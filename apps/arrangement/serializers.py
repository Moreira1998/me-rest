from apps.store.serializers import StoreSerializers

from apps.arrangement.models import Arrangement, TypeOrder, Order, Client, DetailOrder

from rest_framework import serializers


# -------------------------------------------------------->
# Serializers Arrangement


class ArrangementSerializers(serializers.ModelSerializer):
    store = StoreSerializers(many=True)

    class Meta:
        model = Arrangement
        fields = (
            'name',
            'description',
            'ShippingDescription',
            'Store',
        )


# -------------------------------------------------------->
# Serializers TypeOrder


class TypeOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeOrder
        fields = (
            'name',
            'description',
        )


# -------------------------------------------------------->
# Serializers Order


class OrderSerializers(serializers.ModelSerializer):
    typeOrder = TypeOrderSerializers(many=True)

    class Meta:
        model = Order
        fields = (
            'typeOrder',
            'orderData',
            'deliverData',
            'state',
        )


# -------------------------------------------------------->
# Serializers Client


class ClientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'idClient',
            'name',
            'direction',
            'phone1',
            'phone2',
            'email',
        )


# -------------------------------------------------------->
# Serializers DetailOrder


class DetailOrderSerializers(serializers.ModelSerializer):
    Arrangement = ArrangementSerializers(many=True)
    order = OrderSerializers(many=True)
    client = ClientSerializers(many=True)

    class Meta:
        model = DetailOrder
        fields = (
            'arrangement',
            'order',
            'client',
            'price',
            'quantity',
        )