from django.contrib import admin
from .models import ShopDepartment, Category, Brand, Product


@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_editable = ['active']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'brand', 'category']
    list_filter = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category']
    list_filter = ['category']
