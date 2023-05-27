from django import forms
from django.core.exceptions import ValidationError
from .models import (create_nuevo_curso, 
                          create_nuevo_card, 
                          create_nuevo_publicacion, 
                          create_new_consultas ,
                          new_class_hospital ,
                          new_class_servicio)

class CreateNewCard(forms.ModelForm):
    class Meta:
        model = create_nuevo_card
        fields = ['img_card','nombre_card','cargo_card','descrip_card']

    def clean_img_card(self):
        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
        uploaded_image = self.cleaned_data.get("img_card",  False)
        extension = str(uploaded_image).split('.')[-1]
        file_type = extension.lower()
        if not uploaded_image:       
            raise ValidationError("Por favor sube una imagen") # handle empty image

        if file_type not in IMAGE_FILE_TYPES:
            raise ValidationError("El archivo no es una imagen.")
        return uploaded_image
    


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

class CreateNewConsultaRespondido(forms.Form):
     id_respuesta = forms.CharField()
    
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

class validar_delete_consulta(forms.Form):
    id_delete = forms.CharField()
    
class validar_curso_publicar(forms.Form):
    id_curso_pub = forms.CharField()

    

class update_curso(forms.Form):
    curso_actualizar = forms.CharField(max_length=100)
    nombre_curso = forms.CharField(max_length=100)
    descrip_corta_curso = forms.CharField(max_length=250)
    descrip_larga_curso = forms.CharField(max_length=600)
    requisitos_curso = forms.CharField(max_length=100)
    time_start_curso = forms.DateField() 
    time_end_curso = forms.DateField() 
    servicio_curso = forms.CharField(max_length=100)
    hospital_curso = forms.CharField(max_length=100) 
    personal_cursos = forms.CharField(max_length=80)

class update_publicacion(forms.Form):
    id_update = forms.CharField(max_length=100)
    nombre_pub = forms.CharField(max_length=100)
    descrip_pub = forms.CharField(max_length=100)

class update_card(forms.Form):
    id_update = forms.CharField(max_length=100)
    nombre_card = forms.CharField(max_length=100)
    cargo_card = forms.CharField(max_length=100)
    descrip_card = forms.CharField(max_length=100)

class form_filtro_cursos_nombre(forms.Form):
    nombre_curso_buscar = forms.CharField(max_length=100, required=False)

class form_filtro_cursos_time(forms.Form):
    prox_end_curso_buscar = forms.CharField(max_length=100, required=False)

class form_filtro_cursos_servicio(forms.Form):
    servicio_curso_buscar = forms.CharField(max_length=100 ,required=False)

class form_filtro_cursos_hospital(forms.Form):
    hospital_curso_buscar = forms.CharField(max_length=100,required=False)

class form_filtro_cursos_personal(forms.Form):
    personal_curso_buscar = forms.CharField(max_length=100, required=False)

class form_busqueda_consulta_respondidas(forms.Form):
    busqueda_consulta_respondidas = forms.CharField(max_length=100, required=False)

class form_busqueda_consulta(forms.Form):
    busqueda_consulta = forms.CharField(max_length=100, required=False)
class form_busqueda_curso_operador(forms.Form):
    busqueda_curso_operador  = forms.CharField(max_length=100, required=False)