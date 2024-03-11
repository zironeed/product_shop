from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import ProductShopAppConfig
from .views import CategoryListView, ProductListView, CartViewSet

app_name = ProductShopAppConfig.name
router = routers.DefaultRouter()
router.register(f'cart', CartViewSet)

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='cat_list'),
    path('products/', ProductListView.as_view(), name='prod_list'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
