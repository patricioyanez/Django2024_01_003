from django.shortcuts import render
from .models import Alumno
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

    return render(request, 'index.html', context)
