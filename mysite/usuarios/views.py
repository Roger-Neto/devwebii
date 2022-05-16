from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Usuario
from .forms import UsuarioForm

class ListaUsuarioView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nomeCompleto')

class UsuarioCreateView(CreateView):
    model = Usuario 
    form_class = Usuario
    success_url = '/usuario_list/'