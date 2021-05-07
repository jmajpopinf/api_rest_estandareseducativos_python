from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from criterios import views


urlpatterns = [
    path('api/v1/criterionumerico/', views.CriterioNumericoList.as_view()),
    path('api/v1/criterionumerico/<int:pk>', views.CriterioNumericoDetail.as_view()),
    path('api/v1/criterioboleano/', views.CriterioBoleanoList.as_view()),
    path('api/v1/criterioboleano/<int:pk>', views.CriterioBoleanoDetail.as_view()),
    path('api/v1/justificacionbajas/', views.JustifiacionBajasList.as_view()),
    path('api/v1/justificacionbajas/<int:pk>', views.JustifiacionBajasDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)