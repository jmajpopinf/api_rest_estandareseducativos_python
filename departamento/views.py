from rest_framework import generics
from departamento.models import Departamento, Distrito, CentroEducativo, Docente
from departamento.serializer import DepartamentoSerializer, DistritoSerializer, CentroEducativoSerializer, DocenteSerializer

# Create your views here.

class DepartamentoList(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DistritoList(generics.ListCreateAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class DistritoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

class CentroEducativoList(generics.ListCreateAPIView):
    queryset = CentroEducativo.objects.all()
    serializer_class = CentroEducativoSerializer

class CentroEducativoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CentroEducativo.objects.all()
    serializer_class = CentroEducativoSerializer

class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteDetail(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


