from django.db import models

class Pedido(models.Model):

    quantidade = models.IntegerField(default=0, blank=False, null=False)
   
    def __str__(self):
        return f"{self.quantidade}  "