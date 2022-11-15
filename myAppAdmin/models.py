from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    file1 = models.FileField(upload_to='public/', max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

