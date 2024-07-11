from django.contrib import admin
from .models import Aprendiz, Calificaciones, Cursos

# Register your models here.

admin.site.register(Aprendiz)
admin.site.register(Calificaciones)
admin.site.register(Cursos)