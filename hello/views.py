from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Independent, Job
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

    return JsonResponse({'message':message})

@csrf_exempt
def isLoggedUser(request):
    if request.user.is_authenticated():
        logged = True
    else:
        logged = False
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
        independent.job = Job(jsonUser.get('job'))
        independent.job.save()
        independent.save()

    return HttpResponse(serializers.serialize("json",{independent},use_natural_foreign_keys=True, use_natural_primary_keys=True))


@csrf_exempt
def registerIndependent(request):
    if request.method == 'POST':
        objs = json.loads(request.body)

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