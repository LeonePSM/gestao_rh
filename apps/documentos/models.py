from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertencente = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
