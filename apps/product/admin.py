from django.contrib import admin
from apps.product.models import Category, Brand, State, Price, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(State)
admin.site.register(Price)
admin.site.register(Product)
