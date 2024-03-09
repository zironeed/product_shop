from django.urls import path
from apps import ProductShopAppConfig
from views import CategoryListView, ProductListView

app_name = ProductShopAppConfig.name

urlpatterns = [
    path('categories/', CategoryListView.as_view, name='cat_list'),
    path('products/', ProductListView.as_view, name='prod_list'),
]
