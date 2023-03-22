from django.db import models

# Create your models here.

class create_nuevo_curso(models.Model):
    nombre_curso = models.CharField(max_length=30)
    #img_curso =  models.FileField()
    #formulario = models.FileField()
    descripcion_precentacion = models.CharField(max_length=30)
    descripcion_completa = models.CharField(max_length=30)
    requisitos = models.CharField(max_length=30)
    fecha_inicio = models.DateField() 
    fecha_termino = models.DateField() 
    servicios = models.CharField(max_length=30)
    hospital = models.CharField(max_length=30)
    personal = models.CharField(max_length=30)