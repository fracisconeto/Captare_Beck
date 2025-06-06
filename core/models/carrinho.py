
from django.db import models


class Carrinho(models.Model):

    no_carrinho= models.IntegerField(default=0, blank=False, null=False)
    

    def __str__(self):
        return f"{self.cep} "