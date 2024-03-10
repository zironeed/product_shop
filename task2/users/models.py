from django.db import models
from django.conf import settings


class Cart(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='cart_owner')
    products = models.ManyToManyField('Product', through='CartItem')


class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
