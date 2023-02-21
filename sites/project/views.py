from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .serializers import CategorySerializer, UsersSerializer
from  .models import Category, Users
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class CategoryListPanation(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserListPanation(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 300



class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CategoryListPanation


class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly, )

class CategoryDelete(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


#############  users  create

class UsersView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = UserListPanation


class UsersUpdate(RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsOwnerOrReadOnly,)



class UsersDelete(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminOrReadOnly,)



