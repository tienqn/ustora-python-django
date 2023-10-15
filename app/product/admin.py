from django.contrib import admin

from .models import Product, ViewedProduct

admin.site.register(Product)
admin.site.register(ViewedProduct)
