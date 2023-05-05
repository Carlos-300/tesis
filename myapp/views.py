import os

from django.shortcuts import render
from .forms import (CreateNewCursos, 
                    CreateNewCard, 
                    CreateNewPublication,
                    CreateNewHospital,
                    CreateNewServcio,
                    validar_delete_card,
                    validar_delete_cursos,
                    validar_delete_public,
                    validar_curso_publicar,
                    validar_delete_hospital,
                    validar_delete_servicio)
from .models import (create_nuevo_curso, 
                     create_nuevo_card , 
                     create_nuevo_publicacion, 
                     create_new_consultas,
                     new_class_servicio , 
                     new_class_hospital 
                     )

import shutil

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

def lista_consultas_operador(request):
    consultas = create_new_consultas.objects.all()
    for lista in consultas:
        if lista != None:
            return render(request, 'operador/Lista_consultas_cursos.html',{"consultas" :consultas })
    return render(request, 'operador/Lista_consultas_cursos.html',{"consultas" :consultas })


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
    cursos = create_nuevo_curso.objects.all()
    class_hospital = new_class_hospital.objects.all()
    class_serv = new_class_servicio.objects.all()
    for lista in cursos:
        if lista != None:
            return render(request, 'operador/cursos_add.html' ,{"cursos":cursos , "class_hospital" :class_hospital ,"class_serv" :class_serv })
    return render(request, 'operador/cursos_add.html' ,{"cursos":cursos , "class_hospital" :class_hospital ,"class_serv" :class_serv })


#list a str
def convertidor_list_str(list):
    StrA = " ".join(list)
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

            cursos = create_nuevo_curso.objects.all()
            for lista in cursos:
                if lista != None:
                    return render(request, "operador/cursos_add.html" ,{"cursos":cursos })
            return render(request, "operador/cursos_add.html" ,{"cursos":cursos })
        else:
            return render(request, "operador/cursos_add.html", {"ventana": True , "cursos":cursos })
    else:
        return render(request, "operador/cursos_add.html", {"ventana": True , "cursos":cursos })


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
            lista_curos = create_nuevo_curso.objects.all()
            instance = create_nuevo_curso.objects.get(id=id_curso)
            if os.path.isfile("myapp"+instance.img_curso.url) == True:
                os.remove("myapp"+instance.img_curso.url)
            if os.path.isfile("myapp"+instance.form_carga_curso.url) == True:
                os.remove("myapp"+instance.form_carga_curso.url)
            instance.delete()
            return render(request,'operador/cursos_add.html',{"delete_curso":True, "lista_cursos":lista_curos})
        
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

def form_add_hospital(request):
    class_hospital = new_class_hospital.objects.all()
    if request.method == 'POST':
        form = CreateNewHospital(request.POST)
        if form.is_valid():
            model_hospital = new_class_hospital()
            model_hospital.nombre_hospital = request.POST['nombre_hospital']
            model_hospital.save()
            return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})
        return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})
    return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})

def form_add_servicio(request):
    if request.method == 'POST':
        form = CreateNewServcio(request.POST)
        if form.is_valid():
            model_serv = new_class_servicio()
            model_serv.nombre_sev = request.POST['nombre_sev']
            model_serv.save()
            class_serv = new_class_servicio.objects.all()
            return render(request, 'operador/cursos_add.html',{"class_serv" : class_serv})
        
def delete_serv(request):
    if request.method == 'POST':
        form = validar_delete_servicio(request.POST)
        if form.is_valid():
            id_delete = request.POST['id_delete_servicio']
            serv = new_class_hospital.objects.get(id=id_delete)
            serv.delete()
            return
            
        

def delete_hosp(request):
    class_hospital = new_class_hospital.objects.all()
    if request.method == 'POST':
        form = validar_delete_hospital(request.POST)
        if form.is_valid():
            id_delete = request.POST['id_delete_hospital']
            hospit = new_class_hospital.objects.get(id=id_delete)
            hospit.delete()
            return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})
        return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})
    return render(request, 'operador/cursos_add.html',{"class_hospital" : class_hospital})


def form_add_curso_publicidad(request):
    perfil_card = create_nuevo_card.objects.all()
    publicidad = create_nuevo_publicacion.objects.all()
    cursos2 = create_nuevo_curso.objects.all()
    
    if request.method == 'POST':
        form = validar_curso_publicar(request.POST)
        if form.is_valid():
            model_pub = create_nuevo_publicacion()
            id_curso = request.POST['id_curso_pub']
            cursos = create_nuevo_curso.objects.get(id=id_curso)
            
            model_pub.img_pub = cursos.img_curso
            model_pub.nombre_pub = cursos.nombre_curso
            model_pub.descrip_pub = "Finaliza el "+cursos.time_end_curso.strftime("%d-%B-%Y")
            model_pub.save()
            return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad , "cursos" : cursos2})
        return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad , "cursos" : cursos2})
    return render(request, 'operador/mod_index.html',{"perfil_card": perfil_card , "publicidad": publicidad , "cursos" : cursos2})