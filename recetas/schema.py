import graphene
from graphene_django.types import DjangoObjectType
from .models import Receta, Ingrediente, Producto

class RecetaType(DjangoObjectType):
    class Meta:
        model = Receta

class IngredienteType(DjangoObjectType):
    class Meta:
        model = Ingrediente

class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto

class CreateProducto(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        category = graphene.Int(required=True)

    producto = graphene.Field(ProductoType)

    def mutate(self, info, name, category):
        producto = Producto(name=name, category=category)
        producto.save()
        return CreateProducto(producto=producto)

class CreateReceta(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        instructions = graphene.String()
        image = graphene.String()
        difficulty = graphene.Int()
        servings = graphene.Int()
        elaboration_time = graphene.Int()
        cooking_time = graphene.Int()
        ingredientes = graphene.List(graphene.Int)

    receta = graphene.Field(RecetaType)

    def mutate(self, info, name, instructions=None, image=None, difficulty=1, servings=1, elaboration_time=10, cooking_time=10, ingredientes=None):
        receta = Receta(
            name=name,
            instructions=instructions,
            image=image,
            difficulty=difficulty,
            servings=servings,
            elaboration_time=elaboration_time,
            cooking_time=cooking_time
        )
        receta.save()

        if ingredientes:
            for ingrediente_id in ingredientes:
                ingrediente = Ingrediente.objects.get(id=ingrediente_id)
                receta.ingredientes.add(ingrediente)

        return CreateReceta(receta=receta)

class CreateIngrediente(graphene.Mutation):
    class Arguments:
        unit = graphene.Int()
        quantity = graphene.Int()
        producto_id = graphene.Int(required=True)

    ingrediente = graphene.Field(IngredienteType)

    def mutate(self, info, unit=1, quantity=0, producto_id=None):
        producto = Producto.objects.get(id=producto_id)
        ingrediente = Ingrediente(unit=unit, quantity=quantity, producto=producto)
        ingrediente.save()
        return CreateIngrediente(ingrediente=ingrediente)

class Query(graphene.ObjectType):
    all_recetas = graphene.List(RecetaType)
    all_ingredientes = graphene.List(IngredienteType)

    def resolve_all_recetas(self, info, **kwargs):
        return Receta.objects.all()

    def resolve_all_ingredientes(self, info, **kwargs):
        return Ingrediente.objects.all()
    
    def resolve_all_productos(self, info, **kwargs):
        return Producto.objects.all()

class Mutation(graphene.ObjectType):
    create_receta = CreateReceta.Field()
    create_ingrediente = CreateIngrediente.Field()
    create_producto = CreateProducto.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
