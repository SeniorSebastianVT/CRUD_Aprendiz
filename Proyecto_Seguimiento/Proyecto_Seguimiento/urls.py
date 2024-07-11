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
from app_aprendiz.views import inicio, pages_master, aprendices, crear_aprendiz, editar_aprendiz, eliminar_aprendiz, form_aprendiz, calificaciones, cursos

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
    path('cursos/', cursos, name='cursos'),
]
