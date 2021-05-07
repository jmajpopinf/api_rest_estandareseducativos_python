from rol.models import Rol, Usuario, Evaluacion, Permiso, RolPermiso
from rol.serializer import RolSerializer, UsuarioSerializer, EvaluacionSerializer, PermisoSerializer, RolPermisoSerializer
from rest_framework import generics

class RolList(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class PermisoList(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class PermisoDetail(generics.ListCreateAPIView):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer

class RolPermisoList(generics.ListCreateAPIView):
    queryset = RolPermiso.objects.all()
    serializer_class = RolPermisoSerializer

class RolPermisoDetail(generics.ListCreateAPIView):
    queryset = RolPermiso.objects.all()
    serializer_class = RolPermisoSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EvaluacionList(generics.ListCreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

class EvaluacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer



