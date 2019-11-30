from django.db import models
from django.utils.timezone import now


class Testdrive(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Date = models.DateField(default=now)

    def __str__(self):
        return self.Email
    

####