from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.arrangement.viewsets import ArrangementViewSet, TypeOrderViewSet, OrderViewSet, ClientViewSet, DetailOrderViewSet


routers = DefaultRouter()
routers.register(r'', ArrangementViewSet)
routers.register(r'typeOrder', TypeOrderViewSet)
routers.register(r'order', OrderViewSet)
routers.register(r'client', ClientViewSet)
routers.register(r'detailOrder', DetailOrderViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]