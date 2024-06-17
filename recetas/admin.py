from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity','unit')


