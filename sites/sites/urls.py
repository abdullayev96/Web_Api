"""sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from project.views import CategoryView,CategoryUpdate, CategoryDelete, UsersView,UsersUpdate, UsersDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/category/', CategoryView.as_view()),
    path('api/v1/category/<int:pk>/', CategoryUpdate.as_view()),
    path('api/v1/categorydelete/<int:pk>/', CategoryDelete.as_view()),

    path('api/v1/users/', UsersView.as_view()),
    path('api/v1/users/<int:pk>/', UsersUpdate.as_view()),
    path('api/v1/usersdelete/<int:pk>/', UsersDelete.as_view()),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





