from django.contrib import admin
from apps.sale.models import TypeBill, TypeSale, Bill, Sale, DetailSale

# Register your models here.
admin.site.register(TypeBill)
admin.site.register(TypeSale)
admin.site.register(Bill)
admin.site.register(Sale)
admin.site.register(DetailSale)
