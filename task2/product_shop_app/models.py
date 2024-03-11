from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='cat_name', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='cat_slug', unique=True, blank=True)
    image = models.ImageField(upload_to='product_shop/', verbose_name='cat_image')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='sub_name', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='sub_slug', unique=True)
    image = models.ImageField(upload_to='product_shop/', verbose_name='sub_image')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='subcategories')

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='prod_name', unique=True)
    slug = models.SlugField(max_length=100, verbose_name='prod_slug', unique=True)
    price = models.IntegerField(default=0, verbose_name='prod_price')
    image_small = models.ImageField(upload_to='product_shop/', verbose_name='small_image')
    image_mid = models.ImageField(upload_to='product_shop/', verbose_name='mid_image')
    image_big = models.ImageField(upload_to='product_shop/', verbose_name='big_image')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='prod_categories')
    subcategory = models.ForeignKey("Subcategory", on_delete=models.CASCADE, related_name='subcategories',
                                    verbose_name='prod_categories')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='cart_owner')
    products = models.ManyToManyField('Product', through='CartItem')

    def __str__(self): return {self.owner.name}


class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self): return f'{self.product.name} - {self.quantity}'
