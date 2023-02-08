from django.urls import path
from .views import CategoryView, CategoryDetail, CategoryDelete, UsersView, UsersDetail, UsersDelete

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('category/<int:pk>/delete/', CategoryDelete.as_view()),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>/', UsersDetail.as_view()),
    path('users/<int:pk>/delete/', UsersDelete.as_view()),


]