from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.telecom_info)
class telecom_info_admin(admin.ModelAdmin):
    list_display = ["mccmnc", "operator", "country", "mgt", "ngt", "prepaid", "postpaid", "one_network", "code", "tapcode"]
    search_fields = ['mccmnc', 'operator','country', 'mgt', 'ngt','code', 'tapcode']