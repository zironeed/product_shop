from rest_framework import serializers
from .models import Category, Subcategory, Product, Cart, CartItem


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        exclude = ('slug', )


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        exclude = ('slug', )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('slug', )


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
