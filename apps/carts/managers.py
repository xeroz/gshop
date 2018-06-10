from django.db import models
from .querysets import CartQuerySet


class CartManager(models.Manager):

    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)  # Important!

    def new(self):
        return self.new()
