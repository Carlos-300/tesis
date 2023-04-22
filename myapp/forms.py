from django import forms
from myapp.models import create_nuevo_curso, create_nuevo_card, create_nuevo_publicacion


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
        




class validar_delete_card(forms.Form):
    id_delete_card = forms.CharField()

class validar_delete_cursos(forms.Form):
    id_delete_curso = forms.CharField()

class validar_delete_public(forms.Form):
    id_delete_public = forms.CharField()