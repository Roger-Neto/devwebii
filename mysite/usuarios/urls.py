from django.urls import path
from django.urls import URLPattern, path

from .models import Usuario
from .views import ListaUsuarioView, UsuarioCreateView

urlpatterns = [
    path('', ListaUsuarioView.as_view(), name='usuarios.index'),
    path('registrar/', UsuarioCreateView.as_view(), name='usuarios.registro')
]
