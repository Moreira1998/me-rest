from django.contrib import admin
from apps.buy.models import Supplier, TypeBuy, Buy, DetailBuy

# Register your models here.
admin.site.register(Supplier)
admin.site.register(TypeBuy)
admin.site.register(Buy)
admin.site.register(DetailBuy)
