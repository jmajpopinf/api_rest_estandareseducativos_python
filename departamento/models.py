from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombreDepartamento = models.CharField(max_length=50, blank=True)

class Distrito(models.Model):
    nombreDistrito = models.CharField(max_length=50, blank=True)
    deptoDistrito = models.ForeignKey(Departamento, null=True, blank=True, on_delete = models.CASCADE)

class CentroEducativo(models.Model):
    nombreCentro = models.CharField(max_length=50, blank=True)
    direccionCentro = models.CharField(max_length=50, blank=True)
    distritoCentro = models.ForeignKey(Distrito, null=True, blank=True, on_delete = models.CASCADE)

class Docente(models.Model):
    nombreDocente = models.CharField(max_length=50)
    centroEducativo = models.ForeignKey(CentroEducativo, null=True, blank=True, on_delete = models.CASCADE)
