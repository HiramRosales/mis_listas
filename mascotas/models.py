from django.db import models
from django.core.validators import MaxValueValidator

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    edad = models.IntegerField(null = True, validators=[MaxValueValidator(2)])
    peso = models.FloatField(default=0.0)
