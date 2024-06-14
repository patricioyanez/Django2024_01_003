from django.shortcuts import render

from instituto.settings import MEDIA_URL
from .models import Alumno, Carrera, Escuela, Usuario
from .forms import UsuarioForm


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

def eliminarCarrera(request, pk):
    context = {}
    try:
        item = Carrera.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Carrera.objects.all()
    return render(request, 'listarCarrera.html', context)

def eliminarUsuario(request, pk):
    context = {}
    try:
        item = Usuario.objects.get(pk = pk)
        item.delete()
        context['exito'] = "El item fue eliminado"
    except:
        context['error'] = "El item NO fue eliminado"

    context['listado'] = Usuario.objects.all()
    context['form'] = UsuarioForm()
    context['MEDIA_URL'] = MEDIA_URL # AGREGAR: from instituto.settings import MEDIA_URL
    return render(request, 'guardarUsuarioForm.html', context)

def guardarEscuela(request):
    context = {}
    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:
            # validar y capturar except si es necesario
            if len(nombre.strip()) < 1:
                context['error'] = 'No especificó el nombre'
            else:
                if id == "0":
                    Escuela.objects.create(nombre=nombre, activo=activo)        
                else:
                    item = Escuela()
                    item.id = id
                    item.nombre = nombre
                    item.activo = activo
                    item.save()

                context['exito'] = "Los datos fueron guardados"

    return render(request, 'guardarEscuela.html', context)

def guardarCarrera(request):
    context = {}
    context['escuelas'] = Escuela.objects.all()

    if request.method == 'POST':
        idEscuela =  request.POST['cmbEscuela']
        nombre = request.POST['txtNombre']
        version = request.POST['txtVersion']
        activo = 'chkActivo' in request.POST # v o F


        if 'btnGuardar' in request.POST:
            # TAREA: validar y capturar excepciones
            escuela = Escuela.objects.get(pk= idEscuela) # buscar obj según id seleccionado
            Carrera.objects.create(escuela= escuela,
                                    nombre=nombre, 
                                    version=version, 
                                    activo=activo)

            context['exito'] = "Los datos fueron guardados"

    return render(request, 'guardarCarrera.html', context)

def guardarUsuario(request):
    context = {'form': UsuarioForm()}
    if request.method == 'POST':
        if 'btnGuardar' in request.POST:
            form = UsuarioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                context['exito'] = "Los datos fueron guardados"
            else:
                context['error'] = "Error al guardar los datos"
    context['listado'] = Usuario.objects.all()
    context['MEDIA_URL'] = MEDIA_URL # AGREGAR: from instituto.settings import MEDIA_URL
    return render(request, 'guardarUsuarioForm.html', context)

def buscarEscuela(request, pk):
    context = {}
    try:
        item = Escuela.objects.get(pk = pk)
        context['item'] = item
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarEscuela.html', context)

def buscarCarrera(request, pk):
    context = {}
    try:
        context['escuelas'] = Escuela.objects.all()
        context['item'] = Carrera.objects.get(pk = pk)
    except:
        context['error'] = 'Error al buscar el registro'

    return render(request, 'guardarCarrera.html', context)