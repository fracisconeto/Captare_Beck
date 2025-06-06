from django.db import models

class Produto(models.Model):

    nome= models.CharField(max_length=100, blank=False, null=False)
    descrição = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return f"{self.nome}"