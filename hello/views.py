from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Independent, Job, Comment
from django.core.mail import send_mail, EmailMultiAlternatives
import json

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def getIndependents(request):
    independents = Independent.objects.all().order_by('-user__date_joined')
    return HttpResponse(serializers.serialize("json",independents,use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def getProfile(request,id):
    if request.method == 'GET':
        print id
        profile = Independent.objects.all().filter(pk=id)
        print profile
        return HttpResponse(serializers.serialize("json",profile))

@csrf_exempt
def getJobs(request):
    jobs = Job.objects.all()
    return HttpResponse(serializers.serialize("json",jobs))

@csrf_exempt
def loginUser(request):
    message = ''

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))
        username = jsonUser.get('username')
        password = jsonUser.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            message = 'OK'
        else:
            message = 'Usuario y/o clave invalida'
    print message
    print request.user.is_authenticated()
    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
    print logged
    return JsonResponse({'logged':logged})

@csrf_exempt
def logoutUser(request):
    logout(request)
    return JsonResponse({'logout':True})

@csrf_exempt
def profile(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        jsonUser = json.loads(request.body.decode('utf-8'))

        independent.name = jsonUser.get('name')
        independent.lastName = jsonUser.get('last_name')
        independent.yearsOfExperience = jsonUser.get('experience')
        independent.phoneNumber = jsonUser.get('phone_number')
        independent.email = jsonUser.get('email')
        independent.imageFileUrl = jsonUser.get('image')

        jobQS = Job.objects.filter(jobName=str(jsonUser.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def registerIndependent(request):
    print 'antes del request'
    if request.method == 'POST':
        print 'POST'
        objs = json.loads(request.body)
        print objs
        jobString = str(objs['job']).lstrip().rstrip()
        jobQS = Job.objects.filter(jobName=jobString)
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]
        username = objs['username']
        password = objs['password']
        email = objs['email']
        name = objs['name']
        lastName = objs['lastName']
        imageFileUrl = objs['imageFileUrl']
        phoneNumber = objs['phoneNumber']
        yearsOfExperience = objs['yearsOfExperience']

        userModel = User.objects.create_user(username=username, password=password)
        userModel.first_name=name
        userModel.last_name=lastName
        userModel.email=email
        userModel.save()
        print 'Se crea el usuario'

        userQS = User.objects.filter(username=username)
        userList = list(userQS[:1])
        userObject = userList[0]
        independent = Independent()
        independent.email=email
        independent.lastName=lastName
        independent.imageFileUrl=imageFileUrl
        independent.job=jobObject
        independent.name=name
        independent.phoneNumber=phoneNumber
        independent.yearsOfExperience = yearsOfExperience
        independent.user=userObject
        independent.save()
        print 'Se crea el independiente'


    return HttpResponse(status=200)

@csrf_exempt
def registerComment(request):

    if request.method == 'POST':
        objs = json.loads(request.body)
        idIndependent = objs['idIndependent']
        comment = objs['comment']
        userEmail = objs['userEmail']

        comentario = "<strong>Comentario:</strong> %s <br><br><strong>Enviado por:</strong> %s" % (comment, userEmail)

        independent = Independent.objects.get(id=idIndependent)

        emailIndependent = independent.email

        commentModel = Comment()
        commentModel.independent=independent
        commentModel.comment=comentario
        commentModel.userEmail=userEmail
        commentModel.save()

        print 'Se crea comentario para el idIndependent: '+ idIndependent

        #send_mail('Busco Ayuda - Comentario', comentario, userEmail, [emailIndependent], fail_silently=False)

        asunto = 'Busco Ayuda - Comentario'
        text_content = ''
        html_content = comentario
        from_email = userEmail
        to = emailIndependent

        mensaje = EmailMultiAlternatives(asunto, text_content, from_email, [to])
        mensaje.attach_alternative(html_content, "text/html")
        mensaje.send()

        print 'Se envia el correo electronico a: '+ emailIndependent

    return HttpResponse(status=200)


@csrf_exempt
def detail(request):
    user = request.user
    independent = Independent.objects.get(user=user)

    if request.method == 'POST':
        independentJson = json.loads(request.body)
        idIndependent = independentJson['idIndependent']

        independent = Independent.objects.filter(id=idIndependent)

        jobQS = Job.objects.filter(jobName=str(independentJson.get('job')).lstrip().rstrip())
        jobsList = list(jobQS[:1])
        jobObject = jobsList[0]

        independent.job = jobObject
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))
