from django.shortcuts import render
from django.views.generic import ListView
from .models import Usuario


class ListaUsuarioView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nomeCompleto')
