from django.db import models


class ShopDepartmentQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)


class ProductQuerySet(models.QuerySet):

    def related(self, category):
        return self.filter(category=category).order_by('?')[:10]

