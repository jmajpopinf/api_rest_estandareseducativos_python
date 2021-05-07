from django.db import models

# Create your models here.
class Mes(models.Model):
    nombreMes = models.CharField(max_length=50, blank=True)

class Frecuencia(models.Model):
    nombreFrecuencia = models.CharField(max_length=50, blank=True)
    mesFrecuencia = models.ForeignKey(Mes, null=True, blank=True, on_delete = models.CASCADE)
