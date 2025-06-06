from django.db import models

class Categoria(models.Model):

   tipo = models.CharField(max_length=100, blank=False, null=False )
   nome = models.CharField(max_length=100, blank=False, null=False)

def __str__(self):
        return f"{self.nome}  "