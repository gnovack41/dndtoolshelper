import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from dndtoolshelper.api.models import Item


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node,)
        filter_fields = ['name', 'source', 'rarity']
        fields = ['id', 'name', 'source', 'rarity']


class ItemQuery(graphene.ObjectType):
    items = DjangoFilterConnectionField(ItemNode)
