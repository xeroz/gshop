from django.urls import path
from .views import (
    add_cart,
    CartTemplateView
)

app_name = 'carts'

urlpatterns = [
    path('cart/', CartTemplateView.as_view(), name='list'),
    path('add_cart', add_cart, name='add_cart'),
]