from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'create/$', views.create_character),
)