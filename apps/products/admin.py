from django.contrib import admin
from .models import ShopDepartment, Category


@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_editable = ['active']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
