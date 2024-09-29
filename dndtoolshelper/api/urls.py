from django.urls import include, path
from graphene_django.views import GraphQLView
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
