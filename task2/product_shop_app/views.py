from rest_framework.generics import ListAPIView
from serializers import CategorySerializer, ProductSerializer
from models import Product, Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
