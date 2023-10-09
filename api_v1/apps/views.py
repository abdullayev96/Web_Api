from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .models import Childern
from rest_framework import viewsets
from .serializers import ChildernListSerializer, ChildernDetailSerializer, ChildrenSerializer


class ChildernViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Childern.objects.filter(parent__isnull=True)
    serializer_class = ChildernListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ChildernListSerializer
        elif self.action == 'retrieve':
            return ChildernDetailSerializer


class ChildrenBinaryView(viewsets.ReadOnlyModelViewSet):
    queryset = Childern.objects.all()
    serializer_class = ChildrenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'parent_id': ['exact']
    }

    def get_serializer_class(self):
        if self.action == 'list':
            return ChildrenSerializer
