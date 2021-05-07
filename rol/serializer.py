from rest_framework import serializers
from rol.models import Rol, Usuario, Evaluacion, Permiso, RolPermiso

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ('id', 'nombreRol')

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('id', 'nombrePermiso')

class RolPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPermiso
        fields = ('id', 'rolp', 'permisop')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombreUsuario', 'rolUsuario', 'contrasena')

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ('id','idUsuario', 'anio', 'indicador')