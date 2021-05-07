from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rol import views

urlpatterns = [
    path('api/v1/rol/', views.RolList.as_view()),
    path('api/v1/rol/<int:pk>', views.RolDetail.as_view()),
    path('api/v1/permiso/', views.PermisoList.as_view()),
    path('api/v1/permiso/<int:pk>', views.PermisoDetail.as_view()),
    path('api/v1/rolpermiso/', views.RolPermisoList.as_view()),
    path('api/v1/rolpermiso/<int:pk>', views.RolPermisoDetail.as_view()),
    path('api/v1/usuario/', views.UsuarioList.as_view()),
    path('api/v1/usuario/<int:pk>', views.UsuarioDetail.as_view()),
    path('api/v1/evaluacion/', views.EvaluacionList.as_view()),
    path('api/v1/evaluacion/<int:pk>', views.EvaluacionDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
