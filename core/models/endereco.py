from statistics import mode
from django.db import models

class Endereco(models.Model):

    numero = models.IntegerField(default=0, blank=False, null=False)
    rua = models.CharField(max_length=100, blank=False, null=False)
    bairro = models.CharField(max_length=100, blank=False, null=False)
    cep = models.CharField(max_length=8,blank=False, null=False)

    def __str__(self):
        return f"{self.cep}  "