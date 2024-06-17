from django.db import models

class Receta(models.Model):
    name = models.CharField(max_length=150)
    code =  models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.name

class Ingrediente(models.Model):
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=20,blank=True, null=True)
