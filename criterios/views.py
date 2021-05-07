from rest_framework import generics
from criterios.models import CriterioNumerico, CriterioBoleano, JustifiacionBajas
from criterios.serializer import CriterioNumericoSerializer, CriterioBoleanoSerializer, JustifiacionBajasSerializer

# Create your views here.

class CriterioNumericoList(generics.ListCreateAPIView):
    queryset = CriterioNumerico.objects.all()
    serializer_class = CriterioNumericoSerializer

class CriterioNumericoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CriterioNumerico.objects.all()
    serializer_class = CriterioNumericoSerializer

class CriterioBoleanoList(generics.ListCreateAPIView):
    queryset = CriterioBoleano.objects.all()
    serializer_class = CriterioBoleanoSerializer

class CriterioBoleanoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CriterioBoleano.objects.all()
    serializer_class = CriterioBoleanoSerializer

class JustifiacionBajasList(generics.ListCreateAPIView):
    queryset = JustifiacionBajas.objects.all()
    serializer_class = JustifiacionBajasSerializer

class JustifiacionBajasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JustifiacionBajas.objects.all()
    serializer_class = JustifiacionBajasSerializer