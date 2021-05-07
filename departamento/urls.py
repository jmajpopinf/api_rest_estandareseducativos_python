from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from departamento import views




urlpatterns = [
    path('api/v1/departamento/', views.DepartamentoList.as_view()),
    path('api/v1/departamento/<int:pk>', views.DepartamentoDetail.as_view()),
    path('api/v1/distrito/', views.DistritoList.as_view()),
    path('api/v1/distrito/<int:pk>', views.DistritoDetail.as_view()),
    path('api/v1/centroeducativo/', views.CentroEducativoList.as_view()),
    path('api/v1/centroeducativo/<int:pk>', views.CentroEducativoDetail.as_view()),
    path('api/v1/docente/', views.DocenteList.as_view()),
    path('api/v1/docente/<int:pk>', views.DocenteDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)