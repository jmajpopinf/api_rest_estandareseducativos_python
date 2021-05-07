from rest_framework import serializers
from frecuencia.models import Mes, Frecuencia

class MesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mes
        fields = ('id', 'nombreMes')

class FrecuenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frecuencia
        fields = ('id', 'nombreFrecuencia', 'mesFrecuencia')