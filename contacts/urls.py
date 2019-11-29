from django.conf.urls import url
from django.urls import path

import contacts
from contacts import views

app_name = 'contacts'
urlpatterns = [
    url('^$', views.index),
    path(r'leave_feedback',views.leave_feedback,name='leave_feedback'),
]
