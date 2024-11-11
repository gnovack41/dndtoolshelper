from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.filters import BaseFilterBackend, SearchFilter
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

        if 'source' in serializer.validated_data:
            queryset = queryset.filter(source__name__iexact=serializer.validated_data['source'])

        if 'rarity' in serializer.validated_data:
            queryset = queryset.filter(rarity__iexact=serializer.validated_data['rarity'])

        return queryset


class ItemViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.select_related('source').order_by('name').all()

    serializer_class = ItemSerializer
    pagination_class = APIPagination

    search_fields = ['name']

    filter_backends = [SearchFilter, ItemFilter]

    @action(methods=['GET'], detail=False)
    def rarities(self, request):
        return Response(Item.Rarity.values)

    @action(methods=['GET'], detail=False)
    def sources(self, request):
        return Response(list(
            self.queryset.filter(source__isnull=False)
            .values_list('source__name', flat=True)
            .order_by('source__name').distinct('source__name')
        ))
