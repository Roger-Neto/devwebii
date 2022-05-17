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
    
    Usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('auth/cadastro/?status=2')

    if len(usuario) > 0 :
            return redirect('/auth/cadastro/?status=3')
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, sobrenome = sobrenome, email = email, senha = senha)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')    
    except:
        return redirect('auth/cadastro/?status=4')    
    return HttpResponse(f"{nome} {senha} {email}")
