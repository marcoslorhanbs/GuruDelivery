from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250)


class Hamburguer(models.Model):
    productName = models.CharField(max_length=250)
    productLine = models.CharField(max_length=250)
    productDescription = models.TextField(max_length=500)
    productPrice = models.FloatField()
    
    