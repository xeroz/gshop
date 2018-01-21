from django.db import models


class ShopDepartmentQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)
