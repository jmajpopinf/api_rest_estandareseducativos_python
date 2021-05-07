from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from indicadores import views

urlpatterns = [
    path('api/v1/indicador/', views.InicadorList.as_view()),
    path('api/v1/indicador/<int:pk>', views.IndicadorDetail.as_view()),
    path('api/v1/detalleindicador/', views.DetalleIndicadorList.as_view()),
    path('api/v1/detalleindicador/<int:pk>', views.DetalleIndicadorDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

