from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
# Create your views here.


def login(request):
    return HttpResponse('login')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('celular')
    
    usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    usuario.save()
    