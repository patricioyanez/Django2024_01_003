from django.urls import path
from . import views


urlpatterns = [    
    path('', views.menu, name='menu'),# http://127.0.0.1:8000/alumnos/
    path('index', views.index, name='index'),# http://127.0.0.1:8000/alumnos/index
    path('listarAlumnos', views.listarAlumnos, name='listarAlumnos'), 
    ]