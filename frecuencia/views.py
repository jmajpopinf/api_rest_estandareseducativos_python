from rest_framework import generics
from frecuencia.models import Mes, Frecuencia
from frecuencia.serializer import MesSerializer, FrecuenciaSerializer

# Create your views here.

class MesList(generics.ListCreateAPIView):
    queryset = Mes.objects.all()
    serializer_class = MesSerializer

class MesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mes.objects.all()
    serializer_class = MesSerializer

class FrecuenciaList(generics.ListCreateAPIView):
    queryset = Frecuencia.objects.all()
    serializer_class = FrecuenciaSerializer

class FrecuenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Frecuencia.objects.all()
    serializer_class = FrecuenciaSerializer
