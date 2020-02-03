from rest_framework import viewsets
from apps.cellar.models import Cellar, Movement, Inventory, TypeMovement, DetailMovement
from .serializers import CellarSerializers, MovementSerializers, TypeMovementSerializers, InventorySerializers, DetailMovementSerializers
from rest_framework import permissions


#  ------------------------------------------------------->
# ViewSet Cellar


class CellarViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cellar.objects.all()

    def get_serializer_class(self):
        return CellarSerializers


#  ------------------------------------------------------->
# ViewSet Inventory


class InventoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Inventory.objects.all()

    def get_serializer_class(self):
        return InventorySerializers


#  ------------------------------------------------------->
# ViewSet TypeMovement


class TypeMovementViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TypeMovement.objects.all()

    def get_serializer_class(self):
        return TypeMovementSerializers


#  ------------------------------------------------------->
# ViewSet Movement


class MovementViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Movement.objects.all()

    def get_serializer_class(self):
        return MovementSerializers


#  ------------------------------------------------------->
# ViewSet DetailMovement


class DetailMovementViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DetailMovement.objects.all()

    def get_serializer_class(self):
        return DetailMovementSerializers










