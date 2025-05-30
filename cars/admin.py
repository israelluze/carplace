from django.contrib import admin

from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 20


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')
    list_filter = ('factory_year', 'model_year')
    ordering = ('-value',)
    list_per_page = 20

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)