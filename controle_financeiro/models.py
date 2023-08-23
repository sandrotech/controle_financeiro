from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    data = models.DateField(blank=True, null=True)
    movimentacao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.movimentacao
