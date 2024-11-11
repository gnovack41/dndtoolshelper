from django.urls import include, path
from graphene_django.views import GraphQLView
from rest_framework import routers

from dndtoolshelper.api import views

router = routers.SimpleRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('graphql', GraphQLView.as_view(graphiql=True)),
]
