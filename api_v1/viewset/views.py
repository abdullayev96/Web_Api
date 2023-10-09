from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from note.models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from note.serializers import *
from rest_framework.permissions import IsAuthenticated

####### filter
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import CustomPagination




###### Category API
class CategoryListViewSet(ModelViewSet):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer

     pagination_class = CustomPagination

     filter_backends = [filters.SearchFilter]
     search_fields = ['name']

     #filterset_fields = ['name']
     permission_classes = [IsAuthenticated]




class AuthorListViewSet(ModelViewSet):
     queryset = Author.objects.all()
     serializer_class = AuthorSerializer

     filter_backends = [filters.SearchFilter]
     search_fields = ['full_name', 'number_book']

     #filterset_fields = ['full_name', 'number_book']
     #permission_classes = [IsAuthenticated]


class BookListViewSet(ModelViewSet):
     queryset = Book.objects.all()
     serializer_class = BookSerializer

     filter_backends = [filters.SearchFilter]
     search_fields = ['name', 'description']

     #permission_classes = [IsAuthenticated]


