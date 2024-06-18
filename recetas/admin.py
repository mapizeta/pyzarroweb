from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    #list_display = ('name', 'code')
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "ingredientes":
            obj_id = request.resolver_match.kwargs.get('object_id')
            if obj_id:
                receta = Receta.objects.get(id=obj_id)
                kwargs["queryset"] = Ingrediente.objects.filter(tags__contains=[receta.code])
            else:
                kwargs["queryset"] = Ingrediente.objects.none()
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('producto', 'quantity','unit')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
