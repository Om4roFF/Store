from django.db import models
from django.utils.timezone import now


class Testdrive(models.Model):
    male = models.CharField(max_length=10, null=False,default='male')
    name = models.CharField(max_length=30, null=False,default='')
    surname = models.CharField(max_length=30, null=False,default='')
    patronymic = models.CharField(max_length=30 , null=True)
    phone = models.CharField(max_length=12, null=False,default='')
    email = models.EmailField(null=True)
    mark = models.CharField(max_length=50, null=True,default='')
    model = models.CharField(max_length=50, null=False,default='Выберите модель')

    def __str__(self):
        return self.email
