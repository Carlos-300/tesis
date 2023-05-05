from django import forms
from .models import (create_nuevo_curso, 
                          create_nuevo_card, 
                          create_nuevo_publicacion, 
                          create_new_consultas ,
                          new_class_hospital ,
                          new_class_servicio)

class CreateNewCard(forms.ModelForm):
    class Meta:
        model = create_nuevo_card
        fields = '__all__'

class CreateNewPublication(forms.ModelForm):
    class Meta:
        model = create_nuevo_publicacion
        fields = '__all__'

class CreateNewCursos(forms.ModelForm):
    class Meta:
        model = create_nuevo_curso
        fields = '__all__'

class CreateNewHospital(forms.ModelForm):
    class Meta:
            model = new_class_hospital
            fields = '__all__'

class CreateNewServcio(forms.ModelForm):
    class Meta:
        model = new_class_servicio
        fields = '__all__'
        
class CreateNewConsulta(forms.ModelForm):
     class Meta:
        model = create_new_consultas
        fields = '__all__'



class validar_delete_card(forms.Form):
    id_delete_card = forms.CharField()

class validar_delete_cursos(forms.Form):
    id_delete_curso = forms.CharField()

class validar_delete_public(forms.Form):
    id_delete_public = forms.CharField()

class validar_delete_hospital(forms.Form):
    id_delete_hospital = forms.CharField()
class validar_delete_servicio(forms.Form):
    id_delete_servicio = forms.CharField()
    
class validar_curso_publicar(forms.Form):
    id_curso_pub = forms.CharField()

class update_curso(forms.Form):
    nombre_curso = forms.CharField(max_length=100)
    descrip_corta_curso = forms.CharField(max_length=250)
    descrip_larga_curso = forms.CharField(max_length=600)
    requisitos_curso = forms.CharField(max_length=100)
    time_start_curso = forms.DateField() 
    time_end_curso = forms.DateField() 
    servicio_curso = forms.CharField(max_length=100)
    hospital_curso = forms.CharField(max_length=100) 
    personal_cursos = forms.CharField(max_length=80)
