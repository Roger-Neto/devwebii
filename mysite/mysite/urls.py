from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cursos/', include('cursos.urls')),
    path('auth/',include('usuarios.urls')), 
    path('validar_login/', views.validar_login, name = 'validar_login')
    #path('social-auth/', include("social_django.urls", name='social')),
  
]
