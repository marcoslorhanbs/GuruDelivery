from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


