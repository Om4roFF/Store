from sys import path

from django.conf.urls import url

from testdrive import views

urlpatterns = [
    url('^$', views.index),
]