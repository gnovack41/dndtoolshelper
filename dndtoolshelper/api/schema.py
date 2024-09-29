import graphene

from dndtoolshelper.api.queries import ItemQuery


class Query(ItemQuery):
    pass


schema = graphene.Schema(query=Query)
