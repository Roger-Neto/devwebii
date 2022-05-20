from django.shortcuts import render
from django.http import HttpResponse
from .models import CursosDisponiveis
# Create your views here.
def cursos(request):
    cursos = CursosDisponiveis.objects.all()
    return render(request, 'templates/cursos.html', {'cursos': cursos})

def home(request):
    return render(request, 'cursos.html')