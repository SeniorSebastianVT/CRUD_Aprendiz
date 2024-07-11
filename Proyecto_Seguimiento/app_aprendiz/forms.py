from django import forms
from .models import Aprendiz


class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['nombres', 'fecha_nacimiento', 'telefono']