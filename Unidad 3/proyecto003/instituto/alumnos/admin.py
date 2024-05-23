from django.contrib import admin
from .models import Escuela, Carrera, Alumno

# Register your models here.
admin.site.register(Escuela)
admin.site.register(Carrera)
admin.site.register(Alumno)

# ejercicios agregar los otros modelos
# e ingresar 5 filas para cada uno de ellos