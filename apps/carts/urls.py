from django.urls import path
from .views import (
    add_cart,
)

app_name = 'carts'

urlpatterns = [
    path('add_cart', add_cart, name='add_cart'),
]