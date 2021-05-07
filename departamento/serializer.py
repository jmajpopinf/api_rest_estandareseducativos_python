from rest_framework import serializers
from departamento.models import Departamento, Distrito, CentroEducativo, Docente


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombreDepartamento')

class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = ('id', 'nombreDistrito', 'deptoDistrito')

class CentroEducativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroEducativo
        fields = ('id', 'nombreCentro', 'direccionCentro', 'distritoCentro')

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id', 'nombreDocente', 'centroEducativo')

