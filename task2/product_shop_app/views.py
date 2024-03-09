from rest_framework.generics import ListAPIView
from serializers import CategorySerializer, ProductSerializer
from paginators import DefaultPagination
from models import Product, Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = DefaultPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
