from django.urls import path
from django.urls import URLPattern, path
from .views import ListaUsuarioView

urlpatterns = [
    path('', ListaUsuarioView.as_view(), name='usuarios.index' )
]
