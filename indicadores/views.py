from rest_framework import generics
from indicadores.models import Indicador, DetalleIndicador
from indicadores.serializer import IndicadorSerializer, DetalleIndicadorSerializer

# Create your views here.
class InicadorList(generics.ListCreateAPIView):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class IndicadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class DetalleIndicadorList(generics.ListCreateAPIView):
    queryset = DetalleIndicador.objects.all()
    serializer_class = DetalleIndicadorSerializer

class DetalleIndicadorDetail(generics.ListCreateAPIView):
    queryset = DetalleIndicador.objects.all()
    serializer_class = DetalleIndicadorSerializer