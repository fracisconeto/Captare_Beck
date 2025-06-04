from django.db import models

class Usuario(models.Model):

    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11 , blank=False, null=False)
    email = models.EmailField(max_length=100 , blank=False, null=False)
    senha = models.CharField(max_length=45, blank=False, null=False)

    def __str__(self):
        return f"{self.nome} ({self.id}) "