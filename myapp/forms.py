from django import forms
from myapp.models import create_nuevo_curso


class CreateNewCard(forms.Form):
    img = forms.FileField()
    nombre = forms.CharField()
    cargo = forms.CharField()
    descripcion_carta = forms.CharField()

class CreateNewPublication(forms.Form):
    img = forms.FileField()
    nombre_publicacion = forms.CharField()
    descripcion_publicacion = forms.CharField()

    
class CreateNewCursos(forms.Form):
    nombre_curso = forms.CharField()
    #img_curso =  forms.FileField()
    #formulario = forms.FileField()
    descripcion_precentacion = forms.CharField()
    descripcion_completa = forms.CharField()
    requisitos = forms.CharField()
    fecha_inicio = forms.DateField() 
    fecha_termino = forms.DateField() 
    servicios = forms.CharField()
    hospital = forms.CharField()
    personal = forms.CharField()

    class Meta:
        model = create_nuevo_curso
        fields = '__all__'
