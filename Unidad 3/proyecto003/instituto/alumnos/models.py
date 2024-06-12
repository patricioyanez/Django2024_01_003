from django.db import models
# PASOS:
# 1.- definir los modelos
# 2.- preparar la migración
# py manage.py makemigrations alumnos
# 3.- ejecutar la migración (traspaso a la base de datos)
# py manage.py migrate
# 4.- bajar extension: sqlLite3 editor o similar y
# revisar la documentación para ver otros tipos de datos para agregar a models
# 5. continuar con admin.py

# Create your models here.
class Escuela(models.Model):
    nombre      = models.CharField(max_length=100, unique=True)
    activo      = models.IntegerField()

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    escuela     = models.ForeignKey('Escuela', on_delete=models.CASCADE)
    nombre      = models.CharField(max_length=100, unique=True)
    version     = models.IntegerField()
    activo      = models.IntegerField()
    
    def __str__(self):
        return self.escuela.nombre + " : " + self.nombre

class Alumno(models.Model):
    carrera     = models.ForeignKey('Carrera', on_delete=models.CASCADE, db_column='id')
    rut         = models.CharField(primary_key=True, max_length=10)
    dv          = models.CharField(max_length=1)
    nombre      = models.CharField(max_length=50)
    apellido1   = models.CharField(max_length=50)
    apellido2   = models.CharField(max_length=50)
    nacimiento  = models.DateField()
    fono        = models.CharField(max_length=50)
    direccion   = models.CharField(max_length=200)
    email       = models.CharField(max_length=100, unique=True)
    activo      = models.IntegerField()
    
    def __str__(self):
        return self.rut + "-" + self.dv + " " + self.nombre + " " +self.apellido1
    

class Usuario(models.Model):    
    email       = models.CharField(max_length=100, unique=True)    
    nombre      = models.CharField(max_length=50)
    apellido1   = models.CharField(max_length=50)
    apellido2   = models.CharField(max_length=50)
    foto        = models.FileField(upload_to='imagenes/', null=True)
    
    def __str__(self):
        return self.email + " " + self.nombre + " " +self.apellido1 + " " +self.apellido2