from django.views.decorators.csrf import csrf_exempt
from .models import Independent
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'user':request.user}
    return render(request, 'polls/index.html', context)

@csrf_exempt
def getIndependents(request):

    independents = Independent.objects.all().order_by('-user__date_joined')

    return HttpResponse(serializers.serialize("json",independents,use_natural_foreign_keys=True, use_natural_primary_keys=True))