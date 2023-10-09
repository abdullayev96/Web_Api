from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import ListAPIView,  RetrieveAPIView,  CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView, Response



class ListAPI(APIView):
    def get(self, request):

        try:
           category = Category.objects.all()
           serializer  = CategorySerializer(category, many=True)
           return Response(serializer.data)

        except Exception as e:
            print(e)

        return Response({'status':status.HTTP_404_NOT_FOUND})


class CategoryPostApi(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
                  print(e)


        return Response({'status':status.HTTP_404_NOT_FOUND})


class CategoryDetailAPi(APIView):
     def get(self, request, pk=None):
          try:
             cat = Category.objects.get(id=pk)
             serializer   = CategoryDetailSerializer(cat)
             return Response({"data": serializer.data}, status=status.HTTP_200_OK)

          except Exception as e:
                    print(e)


          return Response({"status":status.HTTP_404_NOT_FOUND})


class CategoryUpdateAPI(APIView):

     def put(self, request, pk=None):
            try:
                 user  = Category.objects.get(id=pk)
                 serializer  = CategorySerializer(user, request.data)
                 if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)


            except Exception as e:
                    print(e)

            return Response({"status":status.HTTP_404_NOT_FOUND})


class CategoryDeleteAPI(APIView):
     def delete(self, request, pk=None):
          try:
              user = Category.objects.get(id=pk)
              serializer = CategorySerializer(user, request.data)
              serializer.delete()

              return Response(status=status.HTTP_204_NO_CONTENT)


          except Exception as e:
                    print(e)

          return Response({"status": status.HTTP_404_NOT_FOUND})


######  Crud Category

# class  CategoryAPI(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryCreateAPI(CreateAPIView):
#     queryset  = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
#
# class CategoryUpdateAPI(UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
#
# class CategoryDetailAPI(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer
#
#
# class CategoryDeleteApi(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# ###### Crud Author
#
# class  AuthorAPI(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
#
# class  AuthorDetailAPI(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorDetailSerializer
#
#


