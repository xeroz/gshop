from django.db import models


class InfoSite(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    email = models.EmailField()


class BannerHome(models.Model):
    image = models.URLField()
