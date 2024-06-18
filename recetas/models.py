from django.db import models
from django.contrib.postgres.fields import ArrayField

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

CATEGORY_CHOICES = [
    (1, "Frutas"),
    (2, "Verduras"),
    (3, "Carnes"),
    (4, "Pescados y Mariscos"),
    (5, "Lácteos"),
    (6, "Granos y Legumbres"),
    (7, "Especias y Condimentos"),
    (8, "Aceites y Grasas"),
    (9, "Bebidas"),
    (10, "Otros"),
]

class Producto(models.Model):
    name        = models.CharField(max_length=150)
    category    = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    #brand       = --> Para un futuro desarrollo. Puede incluir la publicidad de alguna marca
    def __str__(self):
        return self.name

class Ingrediente(models.Model):
    producto    = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='ingrediente')
    unit        = models.PositiveSmallIntegerField(choices=UNIT_CHOICES, default=1)
    quantity    = models.IntegerField(default=0)#0 = A gusto Las unidades 0.5 = media,  0.25 = Cuarto, etc
    tags        = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    
    def __str__(self):
        return self.producto.name
    
class Receta(models.Model):
    name                = models.CharField(max_length=150)
    code                = models.CharField(max_length=20,blank=True, null=True)
    image               = models.TextField(blank=True, null=True)
    instructions        = models.TextField(blank=True, null=True)
    difficulty          = models.PositiveSmallIntegerField(choices=DIFFICULT_CHOICES, default=1)
    servings            = models.IntegerField(default=1)
    elaboration_time    = models.IntegerField(default=10)
    cooking_time        = models.IntegerField(default=10)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='recetas', blank=True, null=True)

    def __str__(self):
        return self.name