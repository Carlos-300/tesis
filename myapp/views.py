from django.shortcuts import render
from .forms import CreateNewCursos
from .models import create_nuevo_curso
from django.http import HttpRequest

# Create your views here.
def vistageneral(request):
    return render(request, 'index/index.html')

def lista_cursos_funcionarios(request):
    return render(request, 'index/lista_cursos_fun.html')

def login_operador(request):
    return render(request, 'operador/log_op.html')

def modificar_index(request):
    return render(request, 'operador/mod_index.html')

def ingresar_cursos(request):
    return render(request,'operador/cursos_add.html')

def lista_cursos_operador(request):
    return render(request,'operador/lista_cursos.html')





def form_create_new_curso (request):
    form = CreateNewCursos(request.POST)
    if form.is_valid():
        model_curso = create_nuevo_curso()
        model_curso.nombre_curso = form.cleaned_data['nombre_curso']
        #model_curso.img_curso = form.cleaned_data['img_curso']
        #model_curso.formulario = form.cleaned_data['formulario']
        model_curso.descripcion_precentacion = form.cleaned_data['descripcion_precentacion']
        model_curso.descripcion_completa = form.cleaned_data['descripcion_completa']
        model_curso.requisitos = form.cleaned_data['requisitos']
        model_curso.fecha_inicio = form.cleaned_data['fecha_inicio']
        model_curso.fecha_termino = form.cleaned_data['fecha_termino']
        model_curso.servicios = form.cleaned_data['servicios']
        model_curso.hospital = form.cleaned_data['hospital']
        model_curso.personal = form.cleaned_data['personal']
        print(model_curso.nombre_curso)
        print(form.nombre_curso)
        model_curso.save()
        
        return render(request,"operador/cursos_add.html", {"ventana" : True} )
    else:
        
        print("hola")
        return render(request,"operador/cursos_add.html", {"ventana" : False} )
    
def form_all_cursos()
    return

    






