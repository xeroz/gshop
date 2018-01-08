from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=120)


class ShopDepartment(models.Models):
    name = models.CharField(max_length=50)


class Category(models.Models):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(ShopDepartment)
