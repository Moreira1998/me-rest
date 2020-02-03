from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.cellar.viewsets import CellarViewSet, MovementViewSet, TypeMovementViewSet, InventoryViewSet, DetailMovementViewSet


routers = DefaultRouter()
routers.register(r'', CellarViewSet)
routers.register(r'inventory', InventoryViewSet)
routers.register(r'typeMovement', TypeMovementViewSet)
routers.register(r'movement', MovementViewSet)
routers.register(r'detailMovement', DetailMovementViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]