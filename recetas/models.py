from django.db import models

UNIT_CHOICES = [
    (0, "unit"),
    (1, "gramo"),
    (2, "ml"),
    (3, "kilo"),
    (4, "litro"),
    (5, "cucharada"),
    (6, "cucharadita"),
    (7, "pizca"),
]

DIFFICULT_CHOICES=[
    (1, "baja"),
    (2, "media"),
    (3, "alta"),
    (4, "Master Chef"),
]

class Ingrediente(models.Model):
    name        = models.CharField(max_length=150)
    unit        = models.PositiveSmallIntegerField(choices=UNIT_CHOICES, default=1)
    quantity    = models.IntegerField(default=0)#0 = A gusto Las unidades 0.5 = media,  0.25 = Cuarto, etc

class Receta(models.Model):
    name                = models.CharField(max_length=150)
    code                = models.CharField(max_length=20,blank=True, null=True)
    image               = models.TextField(blank=True, null=True)
    difficulty          = models.PositiveSmallIntegerField(choices=DIFFICULT_CHOICES, default=1)
    servings            = models.IntegerField(default=1)
    elaboration_time    = models.IntegerField(default=10)
    cooking_time        = models.IntegerField(default=10)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='recetas')

    def __str__(self):
        return self.name