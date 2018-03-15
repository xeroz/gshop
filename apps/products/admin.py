from django.contrib import admin
from .models import ShopDepartment, Category, Brand, Product, ImageProduct, DescriptionProduct


@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'top_shop']
    list_editable = ['active', 'top_shop']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'price', 'brand', 'category', 'web_url']
    list_filter = ['category']
    search_fields = ['web_url', 'name']
    list_editable = ['brand']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category']
    list_filter = ['category']


@admin.register(ImageProduct)
class ImageProductAdmin(admin.ModelAdmin):
    pass


@admin.register(DescriptionProduct)
class DescriptionProducttAdmin(admin.ModelAdmin):
    pass
