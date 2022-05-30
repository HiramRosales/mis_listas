from django.db import models

class Carro(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano_creacion = models.IntegerField()
    cap_lts = models.FloatField(default=0.0)

