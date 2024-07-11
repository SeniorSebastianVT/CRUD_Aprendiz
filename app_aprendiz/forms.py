from django import forms
from .models import Aprendiz, Calificaciones, Cursos


class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['nombres', 'fecha_nacimiento', 'telefono']


class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = ['id_calificacion', 'id_aprendiz', 'id_curso', 'nota']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['id_curso', 'id_aprendiz', 'curso']