from django.db import models

# Create your models here.

class create_nuevo_curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    img_curso =  models.ImageField(upload_to="img/cursos" ,null=True, blank=True)
    form_carga_curso = models.FileField(upload_to="documents", null=True, blank=True)
    descrip_corta_curso = models.CharField(max_length=250)
    descrip_larga_curso = models.CharField(max_length=600)
    requisitos_curso = models.CharField(max_length=100)
    time_start_curso = models.DateField() 
    time_end_curso = models.DateField() 
    servicio_curso = models.CharField(max_length=100)
    hospital_curso = models.CharField(max_length=100)
    personal_cursos = models.CharField(max_length=80)

class create_nuevo_card(models.Model):
    img_card =  models.ImageField(upload_to="img/carta",null=True, blank=True)
    nombre_card = models.CharField(max_length=100)
    cargo_card = models.CharField(max_length=100)
    descrip_card = models.CharField(max_length=100)

class create_nuevo_publicacion(models.Model):
    img_pub = models.ImageField(upload_to="img/publicidad",null=True, blank=True)
    nombre_pub = models.CharField(max_length=100)
    descrip_pub = models.CharField(max_length=100, default='SOME STRING')

class create_new_consultas(models.Model):
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)

class new_class_hospital(models.Model):
    nombre_hospital = models.CharField(max_length=250)

class new_class_servicio(models.Model):
    nombre_sev = models.CharField(max_length=250)

class create_new_consultas_respondidas(models.Model):
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    fecha_respuesta = models.DateTimeField()    