from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from frecuencia import views

urlpatterns = [
    path('api/v1/mes/', views.MesList.as_view()),
    path('api/v1/mes/<int:pk>', views.MesDetail.as_view()),
    path('api/v1/frecuencia/', views.FrecuenciaList.as_view()),
    path('api/v1/frecuencia/<int:pk>', views.FrecuenciaDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)