from django.db import models

class Contacts(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Email = models.EmailField()
    Phone = models.CharField(max_length=200)
    Comment = models.TextField()

    def __str__(self):
        return self.Email

    class Meta:
        verbose_name='Контакт'
        verbose_name_plural='Контакты'

