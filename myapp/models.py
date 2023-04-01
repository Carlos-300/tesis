from django.db import models

# Create your models here.

class create_nuevo_curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    img_curso =  models.ImageField(null=True, blank=True)
    form_carga_curso = models.FileField(upload_to="media", null=True, blank=True)
    descrip_corta_curso = models.CharField(max_length=100)
    descrip_larga_curso = models.CharField(max_length=100)
    requisitos_curso = models.CharField(max_length=100)
    time_start_curso = models.DateField() 
    time_end_curso = models.DateField() 
    servicio_curso = models.CharField(max_length=100)
    hospital_curso = models.CharField(max_length=100)
    #personal 
    personal_cursos = models.CharField(max_length=80)



class create_nuevo_card(models.Model):
    img_card =  models.ImageField(null=True, blank=True)
    nombre_card = models.CharField(max_length=100)
    cargo_card = models.CharField(max_length=100)
    descrip_card = models.CharField(max_length=100)

class create_nuevo_publicacion(models.Model):
    img_pub = models.ImageField(null=True, blank=True)
    nombre_pub = models.CharField(max_length=100)
    descrip_pub = models.CharField(max_length=20, default='SOME STRING')

