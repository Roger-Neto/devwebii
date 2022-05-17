from django.db import models

class CursosDisponiveis(models.Model):
    nome_curso = models.CharField(max_length=150)
    professor = models.CharField(max_length=50)
    contato_professor = models.CharField(max_length=30, blank = True, null = True)
    data_curso = models.DateTimeField()

