from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    jobName = models.CharField(max_length=100,blank=True)
    def natural_key(self):
        return self.jobName

class Independent(models.Model):
    name = models.CharField(max_length=100,blank=True)
    lastName = models.CharField(max_length=100,blank=True)
    yearsOfExperience = models.IntegerField(blank=True)
    phoneNumber = models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=100,blank=True)
    imageFileUrl = models.CharField(max_length=1000,blank=True,default='')
    user = models.OneToOneField(User,null=True)
    job = models.ForeignKey(Job,null=True)

class Comment(models.Model):
    independent = models.ForeignKey(Independent,null=True)
    comment = models.CharField(max_length=1000,blank=True)
    userEmail = models.CharField(max_length=50,blank=True)
    created = models.DateTimeField(auto_now_add=True)