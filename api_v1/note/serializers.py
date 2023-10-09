from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model  = Category
          fields  = "__all__"



class CategoryDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model  = Category
          fields  = ['name']



class AuthorSerializer(serializers.ModelSerializer):
     class Meta:
          model  = Author
          fields  = ['id', 'full_name', 'number_book']



class AuthorDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model  = Author
          fields  = ['full_name', 'bio', 'number_book']



class BookSerializer(serializers.ModelSerializer):
     author  = AuthorSerializer()
     category  = CategorySerializer()

     class Meta:
          model  = Book
          fields  = ['id', 'image', 'name', 'author', 'category']



class BookDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model = Book
          fields = ['id', 'image', 'description', 'author', 'category']


