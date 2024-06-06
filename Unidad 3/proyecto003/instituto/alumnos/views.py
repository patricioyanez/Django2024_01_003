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

def ingresarEscuela(request):
    return render(request, 'ingresarEscuela.html', {})

def ingresarCarrera(request):
    escuelas = Escuela.objects.all()
    context = {'escuelas': escuelas}
    return render(request, 'guardarCarrera.html', context)

def eliminarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Escuela.objects.all()
    return render(request, 'listarEscuela.html', context)

def guardarEscuela(request):
    context = {}
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:
            Escuela.objects.create(nombre=nombre, activo=activo)        
            context['exito'] = "Los datos fueron guardados"

    return render(request, 'guardarEscuela.html', context)

def buscarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarEscuela.html', context)