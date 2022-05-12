from django.db import models


class Usuario(models.Model):
    nomeCompleto =  models.CharField(max_length=256)
    dataNascimento = models.DateField(null=False)
    ativa = models.BooleanField(default=True)