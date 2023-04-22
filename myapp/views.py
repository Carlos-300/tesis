import os

from django.shortcuts import render, redirect

from mysite.settings import MEDIA_ROOT
from .forms import (CreateNewCursos, 
                    CreateNewCard, 
                    CreateNewPublication,
                    validar_delete_card,
                    validar_delete_cursos,
                    validar_delete_public)
from .models import create_nuevo_curso, create_nuevo_card , create_nuevo_publicacion
from django.conf import settings
# Create your views here.


def vistageneral(request):
    perfil_card = create_nuevo_card.objects.all()
    publicidad = create_nuevo_publicacion.objects.all()
    cursos = create_nuevo_curso.objects.all()
    return render(request, 'index/index.html',{"perfil_card": perfil_card,"lista_cursos": cursos, "publicidad": publicidad})


def lista_cursos_funcionarios(request):
    cursos = create_nuevo_curso.objects.all()
    for lista in cursos:
        if lista != None:
            return render(request, 'index/lista_cursos_fun.html',{"cursos":cursos })
    return render(request, 'index/lista_cursos_fun.html')

def form_consulta(request):
    return render(request, 'index/consulta_cursos.html')


def login_operador(request):
    return render(request, 'operador/log_op.html')


def modificar_index(request):
    perfil_card = create_nuevo_card.objects.all()
    publicidad = create_nuevo_publicacion.objects.all()
    cursos = create_nuevo_curso.objects.all()
    for lista in cursos:
        if lista != None:
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad, "cursos":cursos })
        
    return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad, "cursos":cursos})


def ingresar_cursos(request):
    return render(request, 'operador/cursos_add.html')

def lista_cursos_operador(request):
    cursos = create_nuevo_curso.objects.all()
    for lista in cursos:
        if lista != None:
            return render(request, 'operador/lista_cursos.html',{"cursos":cursos})
    return render(request, 'operador/lista_cursos.html')


#list a str
def convertidor_list_str(list):
    StrA = " ".join(list)
    print(StrA)
    ## StrA is "a b c"    
    return StrA

#Envio de formularios a la base de datos
def form_create_new_curso(request):
    if request.method == 'POST':
        form = CreateNewCursos(request.POST, request.FILES)
        if form.is_valid():
            lista = request.POST.getlist('personal_cursos')
            model_curso = create_nuevo_curso()
            model_curso.nombre_curso = request.POST['nombre_curso']
            model_curso.img_curso = request.FILES['img_curso']
            model_curso.form_carga_curso = request.FILES['form_carga_curso']
            model_curso.descrip_corta_curso = request.POST['descrip_corta_curso']
            model_curso.descrip_larga_curso = request.POST['descrip_larga_curso']
            model_curso.requisitos_curso = request.POST['requisitos_curso']
            model_curso.time_start_curso = request.POST['time_start_curso']
            model_curso.time_end_curso = request.POST['time_end_curso']
            model_curso.servicio_curso = request.POST['servicio_curso']
            model_curso.hospital_curso = request.POST['hospital_curso']
            #Listado del personal 
            model_curso.personal_cursos = convertidor_list_str(lista)
            model_curso.save()
            
            return render(request, "operador/cursos_add.html")
        else:
            return render(request, "operador/cursos_add.html", {"ventana": True})
    else:
        return render(request, "operador/cursos_add.html", {"ventana": True})


def form_create_new_card(request):
    if request.method == 'POST':
        form = CreateNewCard(request.POST, request.FILES)
        if form.is_valid():
            perfil_card = create_nuevo_card.objects.all()
            publicidad = create_nuevo_publicacion.objects.all()
            model_card = create_nuevo_card()
            model_card.img_card = request.FILES['img_card']
            model_card.nombre_card = request.POST['nombre_card']
            model_card.cargo_card = request.POST['cargo_card']
            model_card.descrip_card = request.POST['descrip_card']
            model_card.save()
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad})
        else: 
            return render(request, "operador/mod_index.html", {"ventana": True})
    else:
        return render(request, "operador/mod_index.html", {"ventana": True})
            
    

def form_create_new_publicacion(request):
    if request.method == 'POST':
        form = CreateNewPublication(request.POST, request.FILES)
        if form.is_valid():
            perfil_card = create_nuevo_card.objects.all()
            publicidad = create_nuevo_publicacion.objects.all()
            model_pub = create_nuevo_publicacion()
            model_pub.img_pub = request.FILES['img_pub']
            model_pub.nombre_pub = request.POST['nombre_pub']
            model_pub.descrip_pub = request.POST['descrip_pub']
            model_pub.save()
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad,'ventana_public':True})
        else:
            return render(request, "operador/mod_index.html", {"ventana": True})
    else:
        return render(request, "operador/mod_index.html", {"ventana": True})
    

#Delete objet de la base de datos
def delete_objet_curso(request):
   if request.method == 'POST':
        form = validar_delete_cursos(request.POST)
        if form.is_valid():
            id_curso = request.POST['id_delete_curso']
            instance = create_nuevo_curso.objects.get(id=id_curso)
            if os.path.isfile("myapp"+instance.img_curso.url) == True:
                os.remove("myapp"+instance.img_curso.url)
            if os.path.isfile("myapp"+instance.form_carga_curso.url) == True:
                os.remove("myapp"+instance.form_carga_curso.url)
            instance.delete()
            return redirect("/lista_cursos_operador/")
        
def delte_objet_card(request):
    if request.method == 'POST':
        form = validar_delete_card(request.POST)
        if form.is_valid():
            perfil_card = create_nuevo_card.objects.all()
            publicidad = create_nuevo_publicacion.objects.all()
            id_card = request.POST['id_delete_card']
            instance = create_nuevo_card.objects.get(id=id_card)
            if os.path.isfile("myapp"+instance.img_card.url) == True:
                os.remove("myapp"+instance.img_card.url)
            instance.delete()
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad})
    
def delte_objet_public(request):
    perfil_card = create_nuevo_card.objects.all()
    publicidad = create_nuevo_publicacion.objects.all()
    if request.method == 'POST':
        form = validar_delete_public(request.POST)
        if form.is_valid():
            id_public = request.POST['id_delete_public']
            instance = create_nuevo_publicacion.objects.get(id=id_public)
            if os.path.isfile("myapp"+instance.img_pub.url) == True:
                os.remove("myapp"+instance.img_pub.url)
            instance.delete()
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad,'ventana_public_delete':True})
        else:
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad,'ventana_public_delete_f':True})
    else:
        return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad,'ventana_public_delete_x':True})



def form_actualizar_curso(request):
    if request.method == 'POST':
        return
    return