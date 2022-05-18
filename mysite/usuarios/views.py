from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256
# Create your views here.


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    usuario = Usuario.objects.filter(email = email)

    usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    usuario.save()


    return HttpResponse(f"{nome} {sobrenome} {senha} {email} ")

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    
    return HttpResponse(f"{email} {senha}")