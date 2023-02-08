from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .serializers import CategorySerializer, UsersSerializer
from  .models import Category, Users


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDelete(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UsersView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDetail(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDelete(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


