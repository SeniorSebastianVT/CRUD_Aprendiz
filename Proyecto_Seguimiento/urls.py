"""
URL configuration for Proyecto_Seguimiento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from app_aprendiz.views import inicio, pages_master, aprendices, crear_aprendiz, editar_aprendiz, eliminar_aprendiz, form_aprendiz, calificaciones, crear_calificacion, editar_calificacion, eliminar_calificacion, form_calificacion, cursos, crear_curso, editar_curso, eliminar_curso, form_curso

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', inicio, name='inicio'),
    path('pages_master/', pages_master, name='pages_master'),

    path('aprendices/', aprendices, name='aprendices'),
    path('crear_aprendiz/', crear_aprendiz, name='crear_aprendiz'),
    path('editar_aprendiz/', editar_aprendiz, name='editar_aprendiz'),
    path('eliminar_aprendiz/<int:id_aprendiz>', eliminar_aprendiz, name='eliminar_aprendiz'),
    path('editar_aprendiz/<int:id_aprendiz>', editar_aprendiz, name='editar_aprendiz'),
    path('form_aprendiz/', form_aprendiz, name='form_aprendiz'),


    path('calificaciones/', calificaciones, name='calificaciones'),
    path('crear_calificacion/', crear_calificacion, name='crear_calificacion'),
    path('editar_calificacion/', editar_calificacion, name='editar_calificacion'),
    path('eliminar_calificacion/<int:id_calificacion>', eliminar_calificacion, name='eliminar_calificacion'),
    path('editar_calificacion/<int:id_calificacion>', editar_calificacion, name='editar_calificacion'),
    path('form_calificacion/', form_calificacion, name='form_calificacion'),


    path('cursos/', cursos, name='cursos'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('editar_curso/', editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:id_curso>', eliminar_curso, name='eliminar_curso'),
    path('editar_curso/<int:id_curso>', editar_curso, name='editar_curso'),
    path('form_curso/', form_curso, name='form_curso'),

]
