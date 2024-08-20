from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year',
                    'owner', 'created_at', 'updated_at',)
    search_fields = ('model', 'brand',)
    list_filter = ('brand',)


admin.site.register(models.Brand, BrandAdmin)
admin.site.register(models.Car, CarAdmin)
