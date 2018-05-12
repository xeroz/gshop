from django.db import models
from .querysets import ShopDepartmentQuerySet, ProductQuerySet


class ShopDepartmentManager(models.Manager):

    def get_queryset(self):
        return ShopDepartmentQuerySet(self.model, using=self._db)  # Important!

    def smaller_than(self):
        return self.all()

    def activate(self):
        return self.get_queryset().active()


class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)  # Important!

    def related(self, category):
        return self.get_queryset().related(category)
