from django.db import models

class Iten(models.Model):

 

    def __str__(self):
        return f"{self.id}"