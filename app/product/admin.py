from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, ViewedProduct

admin.site.register(ViewedProduct)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'origil_price', 'sell_price', 'sold_count', 'added_time')
    list_filter = ('added_time',)

    def display_image(self, obj):

        return mark_safe(f'<img src="#" width="50" height="50" />')

    display_image.short_description = 'Image'