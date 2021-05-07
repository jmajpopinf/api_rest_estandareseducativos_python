from django.db import models

# Create your models here.

class CriterioNumerico(models.Model):
    nombreCriterioN = models.CharField(max_length=100, blank=True)
    numerCriterio = models.IntegerField()
    docCriterio = models.FileField(upload_to='Doc/', default='Doc/None/No-doc.pdf')

class CriterioBoleano(models.Model):
    nombreCriterioB = models.CharField(max_length=100, blank=True)
    SiNo = models.BooleanField(default=False)
    docCriterioB = models.BooleanField(default=False)

class JustifiacionBajas(models.Model):
    nombreBaja = models.CharField(max_length=25)
    SiNo = models.BooleanField(default=False)
