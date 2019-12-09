from django.db import models
from django import forms
from django.forms import formset_factory


class Car(models.Model):
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    drive_unit = models.CharField(max_length=200)
    engine_volume = models.FloatField(max_length=10)
    content = models.TextField(default='')
    short_content = models.TextField(default='')
    img_title = models.ImageField(null=True,blank=True)
    price = models.CharField(max_length=40,default=0,null=False)
    fuel = models.CharField(max_length=40,default='')
    power = models.CharField(max_length=15,default='')
    acceleration = models.CharField(max_length=20,default='')



    def __str__(self):
        return self.model


class Photo(models.Model):
    # image = forms.ImageField(null=True,blank=True,widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    image = models.ImageField(null=True,blank=True)
    cars = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
