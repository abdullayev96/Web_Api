from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ChildrenBinaryView.as_view({'get': 'list'})),
    path('binary/', views.ChildernViewSet.as_view({'get': 'list'})),
    path('detail/<int:pk>/', views.ChildernViewSet.as_view({'get': 'retrieve'})),
]