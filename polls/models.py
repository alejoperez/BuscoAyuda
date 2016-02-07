from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    jobName = models.CharField(max_length=100,blank=True)
    def natural_key(self):
        return self.jobName

class Independent(models.Model):
    imageFile = models.ImageField(upload_to='BuscoAyuda/static/web/images',null=True)
    yearsOfExperience = models.IntegerField(blank=True)
    phoneNumber = models.CharField(max_length=20,blank=True)
    user = models.OneToOneField(User,null=True)
    job = models.ForeignKey(Job,null=True)

class Comment(models.Model):
    independent = models.ForeignKey(Independent,null=True)
    comment = models.CharField(max_length=1000,blank=True)
    userEmail = models.CharField(max_length=50,blank=True)
    created = models.DateTimeField(editable=False,default=timezone.now())
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
