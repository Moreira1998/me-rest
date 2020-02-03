from apps.cellar.models import Cellar, Movement, Inventory, TypeMovement, DetailMovement
from rest_framework import serializers
from apps.product.serializers import ProductSerializers
from apps.store.serializers import StoreSerializers
from apps.staff.serializers import StaffSerializers
# -------------------------------------------------------->
# Serializers Cellar


class CellarSerializers(serializers.ModelSerializer):
    store = StoreSerializers(many=True)

    class Meta:
        model = Cellar
        fields = (
            'name',
            'store',
            'direction',
            'phone',
            'email',
        )


# -------------------------------------------------------->
# Serializers Inventory


class InventorySerializers(serializers.ModelSerializer):
    cellar = CellarSerializers(many=True)
    Product = ProductSerializers(many=True)

    class Meta:
        model = Inventory
        fields = (
            'cellar',
            'Product',
            'quantity',
            'available',

        )


# -------------------------------------------------------->
# Serializers TypeMovement


class TypeMovementSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeMovement
        fields = (
            'name',
            'description',
        )


# -------------------------------------------------------->
# Serializers Movement

class MovementSerializers(serializers.ModelSerializer):
    typeMovement = TypeMovementSerializers(many=True)
    requested = StaffSerializers(many=True)
    approved = StaffSerializers(many=True)
    cellarEntrance = CellarSerializers(many=True)
    cellarExit = CellarSerializers(many=True)

    class Meta:
        model = Movement
        fields = (
            'typeMovement',
            'requested',
            'approved',
            'dateRequested',
            'dateApproved',
            'cellarEntrance',
            'cellarExit',
        )


# -------------------------------------------------------->
# Serializers DetailMovement

class DetailMovementSerializers(serializers.ModelSerializer):
    movement = MovementSerializers(many=True)
    product = ProductSerializers(many=True)

    class Meta:
        model = DetailMovement
        fields = (
            'movement',
            'product',
            'quantity',

        )
