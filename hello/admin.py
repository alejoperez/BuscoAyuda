from django.contrib import admin
from .models import Independent, Job, Comment

# Register your models here.
admin.site.register(Independent)
admin.site.register(Job)
admin.site.register(Comment)