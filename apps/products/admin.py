from django.contrib import admin
from .models import ShopDepartment, Category, Brand


@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_editable = ['active']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
