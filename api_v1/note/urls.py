from django.urls import path
from .views import *


urlpatterns = [
          path('category/', ListAPI.as_view()),
          path('category/create/', CategoryPostApi.as_view()),
          path('category/<int:pk>/',CategoryDetailAPi.as_view()),
          path('category/<int:pk>/update/', CategoryUpdateAPI.as_view()),
          path('category/<int:pk>/delete/', CategoryDeleteAPI.as_view()),


          # path('author/', AuthorAPI.as_view()),
          # path('author/<int:pk>/', AuthorDetailAPI.as_view())

]