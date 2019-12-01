from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    drive_unit = models.CharField(max_length=200)
    engine_volume = models.FloatField(max_length=10)

    def __str__(self):
        return self.model


