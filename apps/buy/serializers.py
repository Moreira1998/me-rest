from rest_framework import serializers
from apps.buy.models import Supplier, TypeBuy, Buy, DetailBuy
from apps.product.serializers import ProductSerializers


# -------------------------------------------------------->
# Serializers Supplier


class SupplierSerializers(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            'idSupplier',
            'name',
            'description',
            'phone'
        )


# -------------------------------------------------------->
# Serializers TypeBuy


class TypeBuySerializers (serializers.ModelSerializer):

    class Meta:
        model = TypeBuy
        fields = (
            'name',
            'description'
        )


# -------------------------------------------------------->
# Serializers Buy


class BuySerializers(serializers.ModelSerializer):
    typeBuy = TypeBuySerializers(many=True)

    class Meta:
        model = Buy
        fields = (
            'idBuy',
            'date',
            'typeBuy',
            'supplier',
        )


# -------------------------------------------------------->
# Serializers DetailBuy


class DetailBuySerializers(serializers.ModelSerializer):
    buy = BuySerializers(many=True)
    supplier = SupplierSerializers(many=True)
    product = ProductSerializers

    class Meta:
        model = DetailBuy
        fields = (
            'buy',
            'product',
            'price',
            'quantity',
        )

