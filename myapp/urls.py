from django.urls import path


from . import views


urlpatterns = [
   
    path('index/', views.vistageneral),
    path('', views.vistageneral),
    path('lista_cursos_fun/', views.lista_cursos_funcionarios),
    path('login_operador/', views.login_operador),
    path('mod_index/',views.modificar_index),
    path('cursos_add/',views.ingresar_cursos),
    path('consultas/',views.lista_consultas_operador),
    path('consultas_cursos/',views.form_consulta),
    #busquedas
    path('filtro_nombre/',views.filtro_cursos_nombre),
    path('filtro_time/',views.filtro_cursos_time),
    path('filtro_servicio/',views.filtro_cursos_servicio),
    path('filtro_hospital/',views.filtro_cursos_hospital),
    path('filtro_personal/',views.filtro_cursos_personal),
    path('busqueda_consulta_respuesta/',views.busqueda_consulta_respondidas),
    path('busqueda_consulta/',views.busqueda_consulta_normal),
    path('busqueda_curso_operador/',views.busqueda_curso_operador),


    #formularios post-- ADD
    path('ingresar_cursos_form/',views.form_create_new_curso),
    path('ingresar_card_form/',views.form_create_new_card),
    path('ingresar_publi_form/',views.form_create_new_publicacion),
    path('public_cursos/',views.form_add_curso_publicidad),
    path('add_hospital/',views.form_add_hospital),
    path('add_servicio/',views.form_add_servicio),
    path('add_consulta/',views.form_add_consulta),
   
    #formularios post-- update
    path('actualizar_curso/',views.form_update_curso),
    path('actualizar_card/',views.form_update_card),
    path('actualizar_public/',views.form_update_public),
    path('respuesta_consulta/',views.form_respuesta_consulta),
    

    #formularios post-- delete
    path('delete_card/',views.delte_objet_card),
    path('delete_curso/',views.delete_objet_curso),
    path('delete_public/',views.delte_objet_public),
    path('delete_hospital/',views.delete_hosp),
    path('delete_servicio/',views.delete_serv),
    path('delete_consulta/',views.delete_consulta),
    path('delete_consulta_respuestas/',views.delete_consulta_respuestas),
    
    
    

    
    

    
   
] 

