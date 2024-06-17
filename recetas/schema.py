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

    receta = graphene.Field(RecetaType)

    def mutate(self, info, name, code=None):
        receta = Receta(name=name, code=code)
        receta.save()
        return CreateReceta(receta=receta)
    
class Query(graphene.ObjectType):
    all_recetas = graphene.List(RecetaType)

    def resolve_all_recetas(self, info, **kwargs):
        return Receta.objects.all()

class Mutation(graphene.ObjectType):
    create_receta = CreateReceta.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)