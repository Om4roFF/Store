from sys import path

from django.conf.urls import url

from testdrive import views


app_name = 'test-drive'
urlpatterns = [
    url('^$', views.index),
    url('add_test-drive',views.add_testdrive,name='add_test-drive'),
]