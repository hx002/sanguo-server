from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'login/$', views.login),
    url(r'register/$', views.register),
)