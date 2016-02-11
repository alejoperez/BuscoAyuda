from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse
from .models import Independent, Job

# Create your views here.
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