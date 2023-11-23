from django.db import models

# Create your models here.

class Actividad(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()