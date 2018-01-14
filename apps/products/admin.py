from django.contrib import admin
from .models import ShopDepartment

@admin.register(ShopDepartment)
class ShopDepartmentAdmin(admin.ModelAdmin):
    pass