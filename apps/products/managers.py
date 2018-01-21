from django.db import models
from .querysets import ShopDepartmentQuerySet


class ShopDepartmentManager(models.Manager):

    def get_queryset(self):
        return ShopDepartmentQuerySet(self.model, using=self._db)  # Important!

    def smaller_than(self):
        return self.all()

    def activate(self):
        return self.get_queryset().active()
