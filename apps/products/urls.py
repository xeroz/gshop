from django.urls import path
from .views import (
    index,
    ProductTemplateView,
    ProductDetailView,
    add_whish_list,
    remove_whish_list
)

app_name = 'products'

urlpatterns = [
    path('index/', index, name='index'),
    path('categories/<slug>/', ProductTemplateView.as_view(), name='list'),
    path('product/<slug>/', ProductDetailView.as_view(), name='detail'),
    path('add_whish_list', add_whish_list, name='add_whish_list'),
    path('remove_whish_list', remove_whish_list, name='remove_whish_list')
]
