from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import ProductShopAppConfig
from .views import CategoryListView, ProductListView, CartAPIView, CartItemDeleteAPIView

app_name = ProductShopAppConfig.name

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='cat_list'),
    path('products/', ProductListView.as_view(), name='prod_list'),

    path('cart/', CartAPIView.as_view(), name='cart_api'),
    path('cart/delete/', CartItemDeleteAPIView.as_view(), name='cart_delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
