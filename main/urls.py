from django.conf.urls import url
from django.urls import path

from main import views

app_name = 'cars'
urlpatterns = [
    url('^$', views.index,name='car_list'),
    path('<int:car_id>/', views.car, name='car'),
    path('images/',views.index,name='images'),
    path('search/', views.search, name='search'),
]