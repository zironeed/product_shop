from django.contrib import admin
from .models import Category, Subcategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('name', 'category',)
    search_fields = ('name', 'category',)

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'subcategory',)
    list_filter = ('name', 'slug', 'category', 'subcategory',)
    search_fields = ('name', 'slug', 'category', 'subcategory',)

    prepopulated_fields = {'slug': ('name',)}
