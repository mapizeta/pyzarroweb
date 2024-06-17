import graphene
from graphene_django.types import DjangoObjectType
from .models import Receta, Ingrediente

class RecetaType(DjangoObjectType):
    class Meta:
        model = Receta

class IngredienteType(DjangoObjectType):
    class Meta:
        model = Ingrediente

class CreateReceta(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        code = graphene.String()
        image = graphene.String()
        difficulty = graphene.Int()
        servings = graphene.Int()
        elaboration_time = graphene.Int()
        cooking_time = graphene.Int()
        ingredientes = graphene.List(graphene.Int)

    receta = graphene.Field(RecetaType)

    def mutate(self, info, name, code=None, image=None, difficulty=1, servings=1, elaboration_time=10, cooking_time=10, ingredientes=None):
        receta = Receta(
            name=name,
            code=code,
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
        name = graphene.String(required=True)
        unit = graphene.Int()
        quantity = graphene.Int()

    ingrediente = graphene.Field(IngredienteType)

    def mutate(self, info, name, unit=1, quantity=0):
        ingrediente = Ingrediente(name=name, unit=unit, quantity=quantity)
        ingrediente.save()
        return CreateIngrediente(ingrediente=ingrediente)

class Query(graphene.ObjectType):
    all_recetas = graphene.List(RecetaType)
    all_ingredientes = graphene.List(IngredienteType)

    def resolve_all_recetas(self, info, **kwargs):
        return Receta.objects.all()

    def resolve_all_ingredientes(self, info, **kwargs):
        return Ingrediente.objects.all()

class Mutation(graphene.ObjectType):
    create_receta = CreateReceta.Field()
    create_ingrediente = CreateIngrediente.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
