from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cursos/', include('cursos.urls')),
    path('auth/',include('usuarios.urls')), 
    #path('social-auth/', include("social_django.urls", name='social')),
  
]
