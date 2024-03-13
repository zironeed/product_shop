from rest_framework import serializers
from .models import Category, Subcategory, Product, CartItem


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
    class Meta:
        model = CartItem
        fields = ('product', 'quantity', )

    def to_representation(self, instance):
        data = ProductSerializer(instance.product).data
        data['quantity'] = instance.quantity

        return data
