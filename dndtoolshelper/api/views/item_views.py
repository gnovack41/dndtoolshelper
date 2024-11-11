from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from dndtoolshelper.api.models import Item
from dndtoolshelper.api.serializers import ItemSerializer
from dndtoolshelper.utils.pagination import APIPagination


class ItemFilter(BaseFilterBackend):
    class ItemFilterSerializer(serializers.Serializer):
        source = serializers.CharField()
        rarity = serializers.CharField()

    def filter_queryset(self, request, queryset, view):
        serializer = self.ItemFilterSerializer(data=request.query_params, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'source' in request.query_params:
            queryset = queryset.filter(source__iexact=request.query_params['source'])

        if 'rarity' in request.query_params:
            queryset = queryset.filter(rarity__iexact=request.query_params['rarity'])

        return queryset


class ItemViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.all()

    serializer_class = ItemSerializer
    pagination_class = APIPagination

    search_fields = ['name']

    filter_backends = [ItemFilter]

    @action(methods=['GET'], detail=False)
    def rarities(self, request):
        return Response(list(self.queryset.filter(rarity__isnull=False).values_list('rarity', flat=True).distinct()))

    @action(methods=['GET'], detail=False)
    def sources(self, request):
        return Response(list(self.queryset.filter(source__isnull=False).values_list('source', flat=True).distinct()))
