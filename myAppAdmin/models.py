from cmath import log
from datetime import date
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    # file = models.FileField(upload_to='public/', max_length=100)
    file = models.FileField()
    date = models.DateField()

    def __str__(self):
        return self.name

