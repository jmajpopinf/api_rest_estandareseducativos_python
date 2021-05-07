from rest_framework import serializers
from criterios.models import CriterioNumerico, CriterioBoleano, JustifiacionBajas

class CriterioNumericoSerializer(serializers.ModelSerializer):
    docCriterio = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = CriterioNumerico
        fields = ('id', 'nombreCriterioN', 'numerCriterio', 'docCriterio')

class CriterioBoleanoSerializer(serializers.ModelSerializer):
    docCriterioB = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = CriterioBoleano
        fields = ('id', 'nombreCriterioB', 'SiNo', 'docCriterioB')
    
class JustifiacionBajasSerializer(serializers.ModelSerializer):
    class Meta:
        model = JustifiacionBajas
        fields = ('id', 'nombreBaja', 'SiNo')