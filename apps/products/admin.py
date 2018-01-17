from django.contrib import admin
from .models import ShopDepartment, Category


@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
