from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.buy.viewsets import SupplierViewSet, TypeBuyViewSet, BuyViewSet, DetailViewSet

routers = DefaultRouter()
routers.register(r'', BuyViewSet)
routers.register(r'typeBuy', TypeBuyViewSet)
routers.register(r'supplier', SupplierViewSet)
routers.register(r'detail', DetailViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]