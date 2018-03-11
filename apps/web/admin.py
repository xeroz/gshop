from django.contrib import admin
from .models import InfoSite, BannerHome
from singlemodeladmin import SingleModelAdmin


@admin.register(InfoSite)
class InfoSiteAdmin(SingleModelAdmin):
    pass


@admin.register(BannerHome)
class BannerHomeAdmin(admin.ModelAdmin):
    pass
