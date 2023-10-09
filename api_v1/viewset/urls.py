from django.urls  import path
from .views import *

from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('category', CategoryListViewSet, basename='category'),
router.register('author', AuthorListViewSet, basename='author')
router.register('book', BookListViewSet, basename='book')
urlpatterns = router.urls