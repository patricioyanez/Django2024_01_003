# Generated by Django 4.2.1 on 2024-06-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_usuario_alter_alumno_email_alter_carrera_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.FileField(null=True, upload_to='imagenes/'),
        ),
    ]