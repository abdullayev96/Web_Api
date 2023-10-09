from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Childern
from .serializers import ChildernListSerializer, ChildernDetailSerializer

class ChildernViewSet(viewsets.ViewSet):

    def list(self, request):
        quertext = Childern.objects.all()
        serializer = ChildernListSerializer(quertext, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        quertext = Childern.objects.all()
        childern = get_object_or_404(quertext, pk=pk)
        serializer = ChildernDetailSerializer(childern)
        return Response(serializer.data)
