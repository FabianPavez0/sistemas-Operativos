from django.db import models

# Create your models here.

class Socio(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    numero_socio = models.IntegerField(unique=True)
    contraseña = models.CharField(max_length=100)
