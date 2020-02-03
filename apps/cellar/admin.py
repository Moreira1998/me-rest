from django.contrib import admin
from apps.cellar.models import Cellar, Movement, Inventory, TypeMovement, DetailMovement

# Register your models here.
admin.site.register(Cellar)
admin.site.register(Movement)
admin.site.register(Inventory)
admin.site.register(TypeMovement)
admin.site.register(DetailMovement)
