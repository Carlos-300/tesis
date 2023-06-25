import os
import shutil
import datetime
from django.http import FileResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DeleteView, UpdateView 
from django.contrib.auth.views import  LoginView
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import (CreateNewCursos,
                    CreateNewCard,
                    CreateNewPublication,
                    CreateNewHospital,
                    CreateNewServcio,
                    CreateNewConsulta,
                    CreateNewConsultaRespondido,
                    validar_delete_card,
                    validar_delete_cursos,
                    validar_delete_public,
                    validar_curso_publicar,
                    validar_delete_hospital,
                    validar_delete_servicio,
                    validar_delete_consulta,
                    update_curso,
                    update_card,
                    update_publicacion,
                    form_filtro_cursos_personal,
                    form_filtro_cursos_nombre,
                    form_filtro_cursos_hospital,
                    form_filtro_cursos_servicio,
                    form_filtro_cursos_time,
                    form_busqueda_consulta,
                    form_busqueda_consulta_respondidas,
                    form_busqueda_curso_operador,
                    UsuarioRegistroForm,
                    LoginForm,
                    form_descarga_postulacion,
                    Update_user,estado_curso)

from .models import (create_nuevo_curso,
                     create_nuevo_card,
                     create_nuevo_publicacion,
                     create_new_consultas,
                     create_new_consultas_respondidas,
                     new_class_servicio,
                     new_class_hospital,
                     Usuario)

def cerrar_todas_sesiones(request):
    try:
        # Cerrar la sesión actual
        logout(request)
        
        # Eliminar todas las sesiones activas del usuario
        session_keys = request.session.keys()
        for key in session_keys:
            del request.session[key]
        
        # Redirigir al usuario a la página de inicio de sesión
        return redirect('/login_operador/')
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir
        print(f"Error al cerrar todas las sesiones: {str(e)}")
    
    # En caso de error, redirigir al usuario a la página de inicio de sesión
    return redirect('/login_operador/')

def is_superuser(user):
    return user.is_staff
    
# list a str
def convertidor_list_str(list):
    StrA = " ".join(list)
    # StrA is "a b c"
    return StrA

# Index vistas generales
def vistageneral(request):
    perfil_card = create_nuevo_card.objects.all().order_by('id')
    publicidad = create_nuevo_publicacion.objects.all().order_by('id')
    cursos = create_nuevo_curso.objects.all().order_by('id')

    return render(request, 'index/index.html', {"perfil_card": perfil_card, "lista_cursos": cursos, "publicidad": publicidad})

def form_consulta(request):
    if request.method == 'POST':
        form = CreateNewConsulta(request.POST)
        if form.is_valid():
            consulta = create_new_consultas()
            consulta.nombre_completo = request.POST['nombre_completo']
            consulta.rut = request.POST['rut']
            consulta.telefono = request.POST['telefono']
            consulta.Correo = request.POST['Correo']
            consulta.save()
            return render(request, 'index/consulta_cursos.html', {"ventana1": True})
        else:
            return render(request, 'index/consulta_cursos.html', {"ventana1_invalid": True ,"form_consulta":form })
    else:
        return render(request, 'index/consulta_cursos.html')


def lista_cursos_funcionarios(request):
    cursos = create_nuevo_curso.objects.filter(activo=True).order_by('id')
    class_hospital = new_class_hospital.objects.all().order_by('id')
    class_serv = new_class_servicio.objects.all().order_by('id')
    #acuerdate de cambiar los cursos aca que esten la fecha caducada


    if request.method == 'POST':
        #filtro busqueda nombre curso
        form = form_filtro_cursos_nombre(request.POST)
        if form.is_valid():
            nombre_curso_buscar = request.POST.get('nombre_curso_buscar')
            if nombre_curso_buscar:
                buscador = create_nuevo_curso.objects.filter(
                    nombre_curso__icontains=nombre_curso_buscar
                    )
                #En caso de no encontrar nada entregamos mensaje de falla
                if buscador.exists() == False:
                    return render(request, 'index/lista_cursos_fun.html', {"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv, "fallafiltro": True})
                return render(request,'index/lista_cursos_fun.html',{"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv})
            
        #Filtro busqueda fecha
        form2 = form_filtro_cursos_time(request.POST)
        if form2.is_valid():
            prox_end_curso_buscar = request.POST.get('prox_end_curso_buscar')
            if prox_end_curso_buscar:
                hoy = datetime.datetime.now() - datetime.timedelta(hours=4)
                fecha_buscar = hoy + \
                    datetime.timedelta(days=int(prox_end_curso_buscar))
                buscador = create_nuevo_curso.objects.filter(
                    time_end_curso__range=(hoy, fecha_buscar))
                #En caso de no encontrar nada entregamos mensaje de falla
                if buscador.exists() == False:
                    return render(request, 'index/lista_cursos_fun.html', {"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv, "fallafiltro": True})
                return render(request,'index/lista_cursos_fun.html',{"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv})
        #Filtro busqueda servicio
        form3 = form_filtro_cursos_servicio(request.POST)
        if form3.is_valid():
            servicio_curso_buscar = request.POST.get('servicio_curso_buscar')
            if servicio_curso_buscar:
                buscador = create_nuevo_curso.objects.filter(
                    servicio_curso=servicio_curso_buscar)
                #En caso de no encontrar nada entregamos mensaje de falla
                if buscador.exists() == False:
                    return render(request, 'index/lista_cursos_fun.html', {"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv, "fallafiltro": True})
                return render(request,'index/lista_cursos_fun.html',{"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv})
        #Filtro de busqueda Hospital
        form4 = form_filtro_cursos_hospital(request.POST)
        if form4.is_valid():
            hospital_curso_buscar = request.POST.get('hospital_curso_buscar')
            if hospital_curso_buscar:
                buscador = create_nuevo_curso.objects.filter(
                    hospital_curso=hospital_curso_buscar)
                #En caso de no encontrar nada entregamos mensaje de falla
                if buscador.exists() == False:
                    return render(request, 'index/lista_cursos_fun.html', {"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv, "fallafiltro": True})
                return render(request,'index/lista_cursos_fun.html',{"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv})
        #Filtro de buqueda personal
        form5 = form_filtro_cursos_personal(request.POST)
        if form5.is_valid():
            personal_curso_buscar = request.POST.get('personal_curso_buscar')
            if personal_curso_buscar:
                buscador = create_nuevo_curso.objects.filter(
                    personal_cursos__icontains=personal_curso_buscar
                    ).distinct()
                #En caso de no encontrar nada entregamos mensaje de falla
                if buscador.exists() == False:
                    return render(request, 'index/lista_cursos_fun.html', {"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv, "fallafiltro": True})
                return render(request,'index/lista_cursos_fun.html',{"cursos": buscador, "class_hospital": class_hospital, "class_serv": class_serv})
        if 'descarga_curso' in request.POST:
            form6 = form_descarga_postulacion(request.POST)
            if form6.is_valid():
                id_buscador = request.POST['id_buscador']
                curso_buscar = create_nuevo_curso.objects.get(id=id_buscador)
                response = FileResponse(curso_buscar.form_carga_curso, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename="{}"'.format(curso_buscar.form_carga_curso)
                return response
           
            
        return render(request, 'index/lista_cursos_fun.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
    else:
        return render(request, 'index/lista_cursos_fun.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})





#Funciones Operador
#vista 
#Cursos & servicios/hospitales
#ingresar/modificar/eliminar/Buscador Cursos & servicios/hospitales
@login_required(login_url='login')
def ingresar_cursos(request):
    cursos = create_nuevo_curso.objects.all().order_by('id')
    class_hospital = new_class_hospital.objects.all().order_by('id')
    class_serv = new_class_servicio.objects.all().order_by('id')
    if request.method == 'POST':


        #ingresar cursos
        if 'curso_ingresado' in request.POST:
            form1 = CreateNewCursos(request.POST, request.FILES)
            if form1.is_valid():
                lista = request.POST.getlist('personal_cursos')
                model_curso = create_nuevo_curso()
                model_curso.nombre_curso = request.POST['nombre_curso']
                model_curso.img_curso = request.FILES.get('img_curso')
                model_curso.form_carga_curso = request.FILES.get('form_carga_curso')
                model_curso.descrip_corta_curso = request.POST['descrip_corta_curso']
                model_curso.descrip_larga_curso = request.POST['descrip_larga_curso']
                model_curso.requisitos_curso = request.POST['requisitos_curso']
                model_curso.time_start_curso = request.POST['time_start_curso']
                model_curso.time_end_curso = request.POST['time_end_curso']
                model_curso.servicio_curso = request.POST['servicio_curso']
                model_curso.hospital_curso = request.POST['hospital_curso']
                # Listado del personal
                model_curso.personal_cursos = convertidor_list_str(lista)
                model_curso.save()

                if cursos.exists() == False:
                        return render(request, "operador/cursos_add.html", {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "form" : form1 ,"curso_add": True, "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "form_addcurso" : form1, "class_hospital": class_hospital, "class_serv": class_serv})
            

        #Activar/Desactivar curso
        if 'bool_curso' in request.POST:
            form_bool = estado_curso(request.POST)
            if form_bool.is_valid():
                id_curso = request.POST['id_curso_estado']
                curso_estado = create_nuevo_curso.objects.get(id=id_curso)
                bool_estado = request.POST['bool_estado_post']
                curso_estado.activo = bool_estado
                curso_estado.save()
                
                if bool_estado == "True":
                    resultado = {"estado" : True, "text" : "El curso se encuentra visible"}
                else:
                    resultado = {"estado" : False, "text" : "El curso se encuentra oculto"}
                

                return render(request, "operador/cursos_add.html", {"cursos": cursos, "lista":True,  "resultado" : resultado , "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})


        
        #Modificar curso
        if 'curso_update' in request.POST:
            form2 = update_curso(request.POST , request.FILES)
            if form2.is_valid():
                id_curso = request.POST['curso_actualizar']
                cursos_encontrado = create_nuevo_curso.objects.get(id=id_curso)
                if 'nombre_curso' in request.FILES:
                    cursos_encontrado.nombre_curso = request.POST['nombre_curso']
                
                if 'img_curso_up' in request.FILES:
                    img_curso_up= request.FILES.get('img_curso_up')
                    instance = cursos_encontrado.img_curso.url
                    if os.path.isfile("myapp"+instance) == True:
                        os.remove("myapp"+instance)
                        cursos_encontrado.img_curso = img_curso_up
                    else:
                        cursos_encontrado.img_curso = img_curso_up
                
                if 'doc_curso_up' in request.FILES:
                    doc_curso_up= request.FILES.get('doc_curso_up')
                    instance = cursos_encontrado.form_carga_curso.url
                    if os.path.isfile("myapp"+instance) == True:
                        os.remove("myapp"+instance)
                        cursos_encontrado.img_curso = doc_curso_up
                    else:
                        cursos_encontrado.img_curso = doc_curso_up
                
                if 'descrip_corta_curso' in request.POST:
                    cursos_encontrado.descrip_corta_curso = request.POST['descrip_corta_curso']
                
                if 'descrip_larga_curso' in request.POST:
                    cursos_encontrado.descrip_larga_curso = request.POST['descrip_larga_curso']
                
                if 'requisitos_curso' in request.POST:
                    cursos_encontrado.requisitos_curso = request.POST['requisitos_curso']
                
                if 'time_start_curso' in request.POST:
                    cursos_encontrado.time_start_curso = request.POST['time_start_curso']
                
                if 'time_end_curso' in request.POST:
                    cursos_encontrado.time_end_curso = request.POST['time_end_curso']
                
                if 'servicio_curso' in request.POST:
                    cursos_encontrado.servicio_curso = request.POST['servicio_curso']
                
                if 'hospital_curso' in request.POST:
                    cursos_encontrado.hospital_curso = request.POST['hospital_curso']
                
                if 'personal_cursos' in request.POST:
                    entrada = request.POST.getlist('personal_cursos')
                    if entrada:
                        cursos_encontrado.personal_cursos = convertidor_list_str(entrada)
                
                cursos_encontrado.save()
            
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "form2" : form2 ,"curso_add": True, "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "form_curso_up" : form2 , "class_hospital": class_hospital, "class_serv": class_serv})

        
        #Eliminar Curso
        if 'curso_delete' in request.POST:
            form3 = validar_delete_cursos(request.POST)
            if form3.is_valid():
                id_curso = request.POST['id_delete_curso']
                try:
                    instance = create_nuevo_curso.objects.get(id=id_curso)
                    if os.path.isfile("myapp"+instance.img_curso.url) == True:
                        os.remove("myapp"+instance.img_curso.url)
                    if os.path.isfile("myapp"+instance.form_carga_curso.url) == True:
                        os.remove("myapp"+instance.form_carga_curso.url)
                    instance.delete()
                except:
                    return render(request, 'operador/cursos_add.html', {"del_curso": True, "cursos": cursos,"lista":True , "class_hospital": class_hospital, "class_serv": class_serv})

                return render(request, 'operador/cursos_add.html', {"del_curso": True, "cursos": cursos,"lista":True , "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, 'operador/cursos_add.html', {"del_curso": True, "cursos": cursos,"lista":True , "class_hospital": class_hospital, "class_serv": class_serv , "form_delete":form3})

        if 'curso_buscador' in request.POST:
            #Busqueda de cursos
            form4 = form_busqueda_curso_operador(request.POST)
            if form4.is_valid():
                busqueda_curso = request.POST.get('busqueda_curso_operador')
                if busqueda_curso:
                    cursos = create_nuevo_curso.objects.filter(
                        Q(nombre_curso__icontains=busqueda_curso) |
                        Q(servicio_curso__icontains=busqueda_curso) |
                        Q(hospital_curso__icontains=busqueda_curso)).distinct()
                    if cursos.exists() == False:
                        cursos = create_nuevo_curso.objects.all()
                        return render(request, "operador/cursos_add.html", {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv,"lista":True,"fail":True})
                    return render(request, "operador/cursos_add.html", {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv,"lista":True})
                return render(request, "operador/cursos_add.html", {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv,"lista":True})
        
        
        #Servicio agregar / eliminar
        
        if 'serv_add' in request.POST:
            #agregar
            form5 = CreateNewServcio(request.POST)
            if form5.is_valid() == True:
                model_serv = new_class_servicio()
                serv_post = request.POST['nombre_sev']
                model_serv.nombre_sev = serv_post
                if new_class_servicio.objects.filter(nombre_sev=serv_post).exists():
                    raise Exception("Ese servicio ya existe")
                else:
                    model_serv.save()
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos,"class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, 'operador/cursos_add.html', {"cursos": cursos,"form_serv":form5,"class_hospital": class_hospital , "class_serv": class_serv})
        
        #eliminar
        if 'serv_delete' in request.POST:
            form6 = validar_delete_servicio(request.POST)
            if form6.is_valid():
                id_delete = request.POST['id_delete_servicio']
                try:
                    serv = new_class_hospital.objects.get(id=id_delete)
                    serv.delete()
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos,"class_hospital": class_hospital , "class_serv": class_serv})
                except:
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos,"class_hospital": class_hospital , "class_serv": class_serv})
            else:
                return render(request, 'operador/cursos_add.html', {"cursos": cursos,"form":form6,"class_hospital": class_hospital , "class_serv": class_serv})
        
        #Hospitales Agregar / eliminar

        #agregar
        if 'hosp_add' in request.POST:
            form7 = CreateNewHospital(request.POST)
            if form7.is_valid():
                model_hospital = new_class_hospital()
                hospital_post = request.POST['nombre_hospital']
                model_hospital.nombre_hospital = hospital_post
                
                if new_class_hospital.objects.filter(nombre_hospital=hospital_post).exists():
                    raise Exception("Ese Hospital ya existe")
                else:
                    model_hospital.save()
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, 'operador/cursos_add.html', {"form_hosp" :form7, "cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
        
        
        #eliminar
        if 'hosp_delete' in request.POST:
            form8 = validar_delete_hospital(request.POST)
            if form8.is_valid():
                id_delete = request.POST['id_delete_hospital']
                try:
                    hospit = new_class_hospital.objects.get(id=id_delete)
                    hospit.delete()
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
                except:
                    return render(request, 'operador/cursos_add.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
            else:
                return render(request, 'operador/cursos_add.html', {"form":form8,"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})
    else:
        return render(request, 'operador/cursos_add.html', {"cursos": cursos, "class_hospital": class_hospital, "class_serv": class_serv})

#Vista de consultas 
#Buscar/eliminar/responder/buscar_respondidas/eliminar_respondidas
@login_required(login_url='login')
def lista_consultas_operador(request):
    consultas = create_new_consultas.objects.all().order_by('id')
    consulta_respuesta2 = create_new_consultas_respondidas.objects.all()
    if request.method == 'POST':
        #busqueda consultas
        if 'filtro_consulta' in request.POST:
            form = form_busqueda_consulta(request.POST)
            if form.is_valid():
                busqueda_consulta = request.POST.get('busqueda_consulta')
                if busqueda_consulta:
                    consultas = create_new_consultas.objects.filter(
                        Q(nombre_completo__icontains=busqueda_consulta) |
                        Q(rut__icontains=busqueda_consulta) |
                        Q(telefono__icontains=busqueda_consulta) |
                        Q(Correo__icontains=busqueda_consulta)
                    ).distinct()
                    if consultas.exists() == False:
                        consultas2 = create_new_consultas.objects.all()
                        return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas2, "consulta_respuesta2": consulta_respuesta2, "fallafiltroconsultas": True})
                return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
            
        #eliminar consulta
        if 'delete_consulta' in request.POST:
            form = validar_delete_consulta(request.POST)
            if form.is_valid():
                id_delete = request.POST['id_delete']
                try:
                    consulta_delete = create_new_consultas.objects.get(id=id_delete)
                    consulta_delete.delete()
                    return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
                except:
                    return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
            else:
                return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})


        #Responder consulta
        if 'from_responder' in request.POST:
            form = CreateNewConsultaRespondido(request.POST)
            if form.is_valid():
                consulta_respuesta = create_new_consultas_respondidas()
                id_respuesta = request.POST['id_respuesta']
                consulta = create_new_consultas.objects.get(id=id_respuesta)
                consulta_respuesta.nombre_completo = consulta.nombre_completo
                consulta_respuesta.rut = consulta.rut
                consulta_respuesta.telefono = consulta.telefono
                consulta_respuesta.Correo = consulta.Correo
                consulta_respuesta.fecha_respuesta = datetime.datetime.now()
                consulta_respuesta.save()
                consulta.delete()
                return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
            else:
                return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
            
        #buscar_respondidas
        if 'busqueda_respondidas' in request.POST:
            form = form_busqueda_consulta_respondidas(request.POST)
            if form.is_valid():
                busqueda_consulta_respondidas = request.POST.get(
                    'busqueda_consulta_respondidas')
                if busqueda_consulta_respondidas:
                    consulta_respuesta2 = create_new_consultas_respondidas.objects.filter(
                        Q(nombre_completo__icontains=busqueda_consulta_respondidas)|
                        Q(rut__icontains=busqueda_consulta_respondidas)|
                        Q(telefono__icontains=busqueda_consulta_respondidas)|
                        Q(Correo__icontains=busqueda_consulta_respondidas)
                    ).distinct()
                    print(consulta_respuesta2.exists())
                    if consulta_respuesta2.exists() == False:
                        consulta_respuesta = create_new_consultas_respondidas.objects.all()
                        return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta, "respuesta": True, "fallafiltroconsultas": True})
                return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2, "respuesta": True})

        #eliminar_respondidas
        if 'delete_respondidas' in request.POST:
            form = validar_delete_consulta(request.POST)
            if form.is_valid():
                id_delete = request.POST['id_delete']
                try:
                    consulta_delete = create_new_consultas_respondidas.objects.get(
                        id=id_delete)
                    consulta_delete.delete()
                    return render(request, 'operador/Lista_consultas_cursos.html', {"respuesta": True,"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
                except:
                    return render(request, 'operador/Lista_consultas_cursos.html', {"respuesta": True,"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})
            else:
                return render(request, 'operador/Lista_consultas_cursos.html', {"respuesta": True,"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})

    else:

        return render(request, 'operador/Lista_consultas_cursos.html', {"consultas": consultas, "consulta_respuesta2": consulta_respuesta2})



#Vista Index 
#Card/Publicidad 
#Ingresa- delete - update -
@login_required(login_url='login')
def modificar_index(request):
    perfil_card = create_nuevo_card.objects.all().order_by('id')
    publicidad = create_nuevo_publicacion.objects.all().order_by('id')
    cursos = create_nuevo_curso.objects.all().order_by('id')
    if request.method == "POST":
        if 'ingresar_card' in request.POST:
            form = CreateNewCard(request.POST, request.FILES)
            if form.is_valid():
                model_card = create_nuevo_card()
                model_card.img_card = request.FILES['img_card']
                model_card.nombre_card = request.POST['nombre_card']
                model_card.cargo_card = request.POST['cargo_card']
                model_card.descrip_card = request.POST['descrip_card']
                model_card.save()
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad,"cursos": cursos ,"card_add": True})
            else:
                return render(request, "operador/mod_index.html", {"form_card" : form, "perfil_card": perfil_card, "publicidad": publicidad,"cursos": cursos})
            
        if 'card_delete' in request.POST:
            form = validar_delete_card(request.POST)
            if form.is_valid():
                id_card = request.POST['id_delete_card']
                try:
                    instance = create_nuevo_card.objects.get(id=id_card)
                    if os.path.isfile("myapp"+instance.img_card.url) == True:
                        os.remove("myapp"+instance.img_card.url)
                    instance.delete()
                    return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad ,"cursos": cursos})
                except:
                    return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad ,"cursos": cursos})
            else:
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad ,"cursos": cursos})
            
        if 'public_ingresa' in request.POST:
            form = CreateNewPublication(request.POST, request.FILES)
            if form.is_valid():
                model_pub = create_nuevo_publicacion()
                model_pub.img_pub = request.FILES['img_pub']
                model_pub.nombre_pub = request.POST['nombre_pub']
                model_pub.descrip_pub = request.POST['descrip_pub']
                model_pub.save()
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, 'ventana_public': True, "public_add": True ,"cursos": cursos})
            else:
                return render(request, 'operador/mod_index.html', {"form_public" : form,"perfil_card": perfil_card, "publicidad": publicidad, 'ventana_public': True ,"cursos": cursos})

        if 'curso_public' in request.POST:  
            form = validar_curso_publicar(request.POST)
            if form.is_valid():
                model_pub = create_nuevo_publicacion()
                id_curso = request.POST['id_curso_pub']
                cursos_2 = create_nuevo_curso.objects.get(id=id_curso)
                head, name = os.path.split(cursos_2.img_curso.name)
                origen = "myapp"+cursos_2.img_curso.url
                destino = "myapp/media/img/public/"+name
                directorio = "myapp/media/img/public"
                if not os.path.exists(directorio):
                    os.makedirs(directorio)
                    shutil.copy(origen, destino)
                else:
                    shutil.copy(origen, destino)
                model_pub.img_pub.name = "img/public/"+name
                model_pub.nombre_pub = cursos_2.nombre_curso
                model_pub.descrip_pub = "Finaliza el " + \
                    cursos_2.time_end_curso.strftime("%d-%B-%Y")
                model_pub.save()
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, "cursos": cursos, 'ventana_public': True}) 
            else:
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, "cursos": cursos, 'ventana_public': True}) 
             
        if 'public_delete' in request.POST:
            form = validar_delete_public(request.POST)
            if form.is_valid():
                id_public = request.POST['id_delete_public']
                print(id_public)
                try:
                    instance = create_nuevo_publicacion.objects.get(id=id_public)
                    if os.path.isfile("myapp"+instance.img_pub.url) == True:
                        os.remove("myapp"+instance.img_pub.url)
                    instance.delete()
                    return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, 'ventana_public_delete': True , "cursos": cursos ,'ventana_public': True})
                except:
                    return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, 'ventana_public_delete': True , "cursos": cursos ,'ventana_public': True})
            else:
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, 'ventana_public_delete': True , "cursos": cursos, 'ventana_public': True})

        if 'card_update' in request.POST:
            form = update_card(request.POST , request.FILES)
            if form.is_valid():
                id_update = request.POST['id_update']
                card = create_nuevo_card.objects.get(id=id_update)
                if 'nombre_card' in request.POST:
                    card.nombre_card = request.POST['nombre_card']
                if 'cargo_card' in request.POST:
                    card.cargo_card = request.POST['cargo_card']
                if 'descrip_card' in request.POST:
                    card.descrip_card = request.POST['descrip_card']
                if 'img_card_up' in  request.FILES:
                    img_card_up = request.FILES.get('img_card_up')
                    instance = card.img_card.url
                    if os.path.isfile("myapp"+instance) == True:
                        os.remove("myapp"+instance)
                        card.img_card = img_card_up
                    else:
                        card.img_card = img_card_up
                card.save()
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad , "cursos": cursos})
            else:
                return render(request, 'operador/mod_index.html', {"form_card_up":form,"perfil_card": perfil_card, "publicidad": publicidad , "cursos": cursos})
            
        if 'public_update' in request.POST:
            form = update_publicacion(request.POST, request.FILES)
            if form.is_valid():
                id_update = request.POST['id_update_pub']
                public = create_nuevo_publicacion.objects.get(id=id_update)
                if 'nombre_pub' in request.POST:
                    public.nombre_pub = request.POST['nombre_pub']
                if 'descrip_pub' in request.POST:
                    public.descrip_pub = request.POST['descrip_pub']
                if 'img_pub_up' in  request.FILES:
                    img_pub_up = request.FILES.get('img_pub_up')
                    instance = public.img_pub.url
                    if os.path.isfile("myapp"+instance) == True:
                        os.remove("myapp"+instance)
                        public.img_pub = img_pub_up
                    else:
                        public.img_pub = img_pub_up
                public.save()
                return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad , "cursos": cursos, 'ventana_public': True})
            else:
                return render(request, 'operador/mod_index.html', {"form_public_up":form,"perfil_card": perfil_card, "publicidad": publicidad , "cursos": cursos, 'ventana_public': True})
    else:
        return render(request, 'operador/mod_index.html', {"perfil_card": perfil_card, "publicidad": publicidad, "cursos": cursos})
    


def logout_view(request):
    session_key = request.session.session_key
    Session.objects.filter(session_key=session_key).delete()
    logout(request)
    return redirect('login')


#Vista admin
#es el unico que puede registrar
@login_required(login_url='login')
@user_passes_test(is_superuser , login_url='/mod_index/')
def registrar(request):
    usuarios = Usuario.objects.all().order_by('id')
    form = UsuarioRegistroForm()
    if request.method == "POST":
        if 'create_user' in request.POST:
            form_create_user = UsuarioRegistroForm(request.POST)
            if form_create_user.is_valid():
                form_create_user.save()
                return render(request, "operador/personal.html" ,{"form_register":form_create_user ,"usuarios":usuarios})
            else:
                return render(request, "operador/personal.html" ,{"form_register":form_create_user ,"usuarios":usuarios})
            
       
    else:
        return render(request, "operador/personal.html" ,{"form_register":form ,"usuarios":usuarios})


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'operador/delete_usuario.html'
    success_url = reverse_lazy('/personal/')


class UserUpdateView(UpdateView):
    model = Usuario
    form_class = Update_user
    template_name = 'operador/update_usuario.html'

    def dispatch(self,request,*args ,**kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/mod_index/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            user_update = self.get_object()
            user_update.email = request.POST['email']
            user_update.celular = request.POST['celular']
            user_update.nombres = request.POST['nombres']
            user_update.username = request.POST['username']
            if 'user_password_up' in request.POST:
                user_update.set_password(request.POST['password'])
            user_update.save()
            return redirect('personal')
        else:
            return redirect('personal')

class CustomLoginView(LoginView):
    template_name = 'operador/log_op.html'
    form_class= LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/mod_index/'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/mod_index/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/mod_index/')
            else:
                form.add_error(None, 'Credenciales inválidas')
        return render(request, self.template_name, {'form': form})


def pagina_no_encontrada(request, route):
    if request.method == "POST":
        if 'my_button' in request.POST:
            if request.user.is_authenticated:
                return redirect('/mod_index/')
            else:
                return redirect('/index/')
    else:
        return render(request, 'error/error_404.html')
   

   