from django.db import models
from indicadores.models import Indicador

# Create your models here.
class Rol(models.Model):
    nombreRol = models.CharField(max_length=100, blank=True)

class Permiso(models.Model):
    nombrePermiso = models. CharField(max_length=500, blank=True)

class RolPermiso(models.Model):
    rolp = models.ForeignKey(Rol, null=True, blank = True, on_delete = models.CASCADE)
    permisop = models.ForeignKey(Permiso, null=True, blank = True, on_delete = models.CASCADE)

class Usuario(models.Model):
    rolUsuario = models.ForeignKey(Rol, null=True, blank = True, on_delete = models.CASCADE)
    nombreUsuario = models.CharField(max_length=100, blank=True)
    contrasena = models.CharField(max_length=25, blank=False)


class Evaluacion(models.Model):
    idUsuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete = models.CASCADE)
    anio = models.IntegerField()
    indicador = models.ForeignKey(Indicador, null=True, blank=True, on_delete = models.CASCADE)






