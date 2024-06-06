from django.urls import path
from . import views


urlpatterns = [    
    path('', views.menu, name='menu'),# http://127.0.0.1:8000/alumnos/
    path('index', views.index, name='index'),# http://127.0.0.1:8000/alumnos/index
    path('listarAlumnos', views.listarAlumnos, name='listarAlumnos'), 
    path('listarCarrera', views.listarCarrera, name='listarCarrera'), 
    path('listarEscuela', views.listarEscuela, name='listarEscuela'), 
    path('ingresarEscuela', views.ingresarEscuela, name='ingresarEscuela'), 
    path('ingresarCarrera', views.ingresarCarrera, name='ingresarCarrera'), 
    path('eliminarEscuela/<str:pk>', views.eliminarEscuela, name='eliminarEscuela'), 
    path('buscarEscuela/<str:pk>', views.buscarEscuela, name='buscarEscuela'), 
    path('guardarEscuela', views.guardarEscuela, name='guardarEscuela'), 

    ]