from turtle import home
from django.urls import URLPattern, path
from .views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home')
]
