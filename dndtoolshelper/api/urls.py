from django.urls import include, path
from graphene_django.views import GraphQLView
from rest_framework import routers

from dndtoolshelper.api import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'items', views.ItemViewSet)
router.register(r'characters', views.CharacterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
