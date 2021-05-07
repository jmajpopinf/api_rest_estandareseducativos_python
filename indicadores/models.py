from django.db import models
from criterios.models import CriterioNumerico, CriterioBoleano, JustifiacionBajas
from frecuencia.models import Frecuencia, Mes
from departamento.models import Departamento, Distrito, CentroEducativo, Docente

# Create your models here.

class Indicador(models.Model):
    nombreIndicador = models.CharField(max_length=200, blank=True)
    descIndicador = models.CharField(max_length=500, blank=True)

class DetalleIndicador(models.Model):
    indicador = models.ForeignKey(Indicador, null=True, blank=True, on_delete = models.CASCADE)
    criterioNumerico = models.ForeignKey(CriterioNumerico, null=True, blank=True, on_delete = models.CASCADE)
    criterioBoleano = models.ForeignKey(CriterioBoleano, null=True, blank=True, on_delete = models.CASCADE)
    bajas = models.ForeignKey(JustifiacionBajas, null=True, blank=True, on_delete = models.CASCADE)
    frecuencia = models.ForeignKey(Frecuencia, null=True, blank=True, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete = models.CASCADE)
    docIndicador = models.FileField(upload_to='Doc/', default='Doc/None/No-doc.pdf')
