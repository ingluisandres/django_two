from django.db import models

# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundations = models.PositiveBigIntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()