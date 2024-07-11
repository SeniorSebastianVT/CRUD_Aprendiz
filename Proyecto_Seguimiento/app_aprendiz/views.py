from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz
from .forms import AprendizForm

# Create your views here.

def inicio(request):
  return render(request, 'app_aprendiz/inicio.html')

def pages_master(request):
  return render(request, 'app_aprendiz/pages_master.html')

def aprendices(request):
  aprendices = Aprendiz.objects.all
  return render(request, 'app_aprendiz/aprendiz.html', {'aprendices': aprendices})

def crear_aprendiz(request):
  formulario_aprendiz = AprendizForm(request.POST or None)
  if formulario_aprendiz.is_valid():
    formulario_aprendiz.save()
    return redirect('aprendices')
  return render(request, 'app_aprendiz/crear_aprendiz.html', {'formulario_aprendiz': formulario_aprendiz})

def editar_aprendiz(request, id_aprendiz):
  aprendiz = get_object_or_404(Aprendiz, id_aprendiz=id_aprendiz)
  formulario_aprendiz = AprendizForm(instance=aprendiz)
  if request.POST == 'POST': 
    formulario_aprendiz = AprendizForm(request.POST, instance=aprendiz)
    if formulario_aprendiz.is_valid():
      formulario_aprendiz.save()
  return render(request, 'app_aprendiz/editar_aprendiz.html', {'formulario_aprendiz': formulario_aprendiz})


def eliminar_aprendiz(request, id_aprendiz):
  aprendiz = get_object_or_404(Aprendiz, id_aprendiz=id_aprendiz)
  aprendiz.delete()
  return redirect(request, 'aprendices')

def form_aprendiz(request):
  return render(request, 'app_aprendiz/form_aprendiz.html')




def calificaciones(request):
  return render(request, 'app_aprendiz/calificacion.html')

def cursos(request):
  return render(request, 'app_aprendiz/curso.html')
