from django.db.models import Sum
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer
from .paginators import DefaultPagination
from .models import Product, Category, Cart, CartItem


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = DefaultPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination


class CartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Информация о товарах в корзине
        """
        cart = request.user.cart
        cart_items = CartItem.objects.filter(cart=cart)

        total_quantity = cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        total_price = sum(item.product.price * item.quantity for item in cart_items)

        cart_content = {
            'total_quantity': total_quantity or 0,
            'total_price': total_price or 0,
            'items': CartItemSerializer(cart_items, many=True).data
        }

        return Response(cart_content)

    def post(self, request):
        id = request.data['id']
        quantity = request.data['quantity']

        cart, created = Cart.objects.update_or_create(owner=request.user)
        print(cart, created)

        product = Product.objects.get(id=id)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        print(cart_item, created)
        cart_item.save()

        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=201)

    def delete(self, request):
        id = request.data['id']
        quantity = request.data['quantity']

        cart = request.user.cart
        product = Product.objects.get(id=id)
        cart_item = CartItem.objects.get(cart=cart, product=product)

        if cart_item.quantity > quantity:
            cart_item.quantity -= quantity
            cart_item.save()
        else:
            cart_item.delete()

        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data)


class CartItemDeleteAPIView(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        cart = request.user.cart
        cart_items = CartItem.objects.filter(cart=cart)

        cart_items.all().delete()

        return Response({'message': 'OK'})
