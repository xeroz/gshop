from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        related_name='carts',
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        Product,
        related_name='products',
        blank=True,
    )
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
