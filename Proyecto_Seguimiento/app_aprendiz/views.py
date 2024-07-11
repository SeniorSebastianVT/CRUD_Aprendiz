from django.shortcuts import render, get_object_or_404, redirect
from .models import Aprendiz, Calificaciones, Cursos
from .forms import AprendizForm, CalificacionForm, CursoForm

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
  calificaciones = Calificaciones.objects.all
  return render(request, 'app_aprendiz/calificacion.html', {'calificaciones': calificaciones})

def crear_calificacion(request):
  formulario_calificacion = CalificacionForm(request.POST or None)
  if formulario_calificacion.is_valid():
    formulario_calificacion.save()
    return redirect('calificaciones')
  return render(request, 'app_aprendiz/crear_calificacion.html', {'formulario_calificacion': formulario_calificacion})

def editar_calificacion(request, id_calificacion):
  calificacion = get_object_or_404(Calificaciones, id_calificacion=id_calificacion)
  formulario_calificacion = CalificacionForm(instance=calificacion)
  if request.POST == 'POST': 
    formulario_calificacion = CalificacionForm(request.POST, instance=calificacion)
    if formulario_calificacion.is_valid():
      formulario_calificacion.save()
  return render(request, 'app_aprendiz/editar_calificacion.html', {'formulario_calificacion': formulario_calificacion})


def eliminar_calificacion(request, id_calificacion):
  calificacion = get_object_or_404(Calificaciones, id_calificacion=id_calificacion)
  calificacion.delete()
  return redirect(request, 'calificaciones')

def form_calificacion(request):
  return render(request, 'app_aprendiz/form_calificacion.html')





def cursos(request):
  cursos = Cursos.objects.all
  return render(request, 'app_aprendiz/curso.html', {'cursos': cursos})

def crear_curso(request):
  formulario_curso = CursoForm(request.POST or None)
  if formulario_curso.is_valid():
    formulario_curso.save()
    return redirect('cursos')
  return render(request, 'app_aprendiz/crear_curso.html', {'formulario_curso': formulario_curso})

def editar_curso(request, id_curso):
  curso = get_object_or_404(Cursos, id_curso=id_curso)
  formulario_curso = CursoForm(instance=curso)
  if request.POST == 'POST': 
    formulario_curso = CursoForm(request.POST, instance=curso)
    if formulario_curso.is_valid():
      formulario_curso.save()
  return render(request, 'app_aprendiz/editar_curso.html', {'formulario_curso': formulario_curso})


def eliminar_curso(request, id_curso):
  curso = get_object_or_404(Cursos, id_curso=id_curso)
  curso.delete()
  return redirect(request, 'cursos')

def form_curso(request):
  return render(request, 'app_aprendiz/form_curso.html')