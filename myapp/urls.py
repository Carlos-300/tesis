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
    
    
    #formularios post
    path('ingresar_cursos_form/',views.form_create_new_curso),
    path('ingresar_card_form/',views.form_create_new_card),
    path('ingresar_publi_form/',views.form_create_new_publicacion),
    path('delete_card/',views.delte_objet_card),
    path('delete_curso/',views.delete_objet_curso),
    path('delete_public/',views.delte_objet_public),
    path('consultas_cursos/',views.form_consulta),
    path('public_cursos/',views.form_add_curso_publicidad),

    #add hospital servicio
    path('add_hospital/',views.form_add_hospital),
    path('add_servicio/',views.form_add_servicio),
    path('delete_hospital/',views.delete_hosp),
    path('delete_servicio/',views.delete_serv),
    
    

    
   
] 

