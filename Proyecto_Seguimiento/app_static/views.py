from django.shortcuts import render

# Create your views here.

def inicio(request):
  return render(request, 'app_static/inicio.html')

def pages_master(request):
  return render(request, 'app_static/pages_master.html')