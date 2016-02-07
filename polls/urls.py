from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^independents/$', views.getIndependents, name='independents'),
]