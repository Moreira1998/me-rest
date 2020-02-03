from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.sale.viewsets import TypeBillViewSet, TypeSaleViewSet, BillViewSet, SaleViewSet, DetailSaleViewSet


routers = DefaultRouter()
routers.register(r'', SaleViewSet)
routers.register(r'typeBill', TypeBillViewSet)
routers.register(r'typeSale', TypeSaleViewSet)
routers.register(r'bill', BillViewSet)
routers.register(r'detailSale', DetailSaleViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]