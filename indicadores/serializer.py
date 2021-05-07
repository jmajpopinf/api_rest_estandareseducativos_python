from rest_framework import serializers
from indicadores.models import Indicador, DetalleIndicador

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = ('id', 'nombreIndicador', 'descIndicador')

class DetalleIndicadorSerializer(serializers.ModelSerializer):
    docIndicador = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = DetalleIndicador
        fields = ('id', 'indicador', 'criterioNumerico', 'criterioBoleano', 'bajas', 'frecuencia', 'departamento', 'docIndicador')