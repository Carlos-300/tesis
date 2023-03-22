from django.urls import path


from . import views


urlpatterns = [
   
    path('index/', views.vistageneral),
    path('', views.vistageneral),
    path('lista_cursos_fun/', views.lista_cursos_funcionarios),
    path('login_operador/', views.login_operador),
    path('mod_index/',views.modificar_index),
    path('cursos_add/',views.ingresar_cursos),
    path('lista_cursos_operador/',views.lista_cursos_operador),
    #formularios post
    path('ingresar_cursos_form/',views.form_create_new_curso),
   
]