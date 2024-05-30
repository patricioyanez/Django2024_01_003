from django.shortcuts import render
from .models import Alumno, Carrera, Escuela
# Create your views here.
def menu(request):
    return render(request, 'plantillaBase.html', {})

def index(request):
    alumnos = Alumno.objects.all() # select * from alumno
    context = {"alumnos":alumnos}
    print(alumnos)
    return render(request, 'index.html', context)

def listarAlumnos(request):
    # utilizar ORM de Django
    # select * from alumno
    alumnos = Alumno.objects.all()

    context = {'alumnos': alumnos}

    return render(request, 'listarAlumnos.html', context)

def listarCarrera(request):
    listado = Carrera.objects.all()
    context = {'listado': listado}
    return render(request, 'listarCarrera.html', context)

def listarEscuela(request):
    listado = Escuela.objects.all()
    context = {'listado': listado}
    return render(request, 'listarEscuela.html', context)
