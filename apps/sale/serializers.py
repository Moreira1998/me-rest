from rest_framework import serializers
from apps.sale.models import TypeBill, TypeSale, Bill, Sale, DetailSale
from apps.store.serializers import StoreSerializers
from apps.product.serializers import ProductSerializers


# ------------------------------------------------------------------------------------>
# Serializers TypeBill


class TypeBillSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeBill
        fields = (
            'name',
            'description',
        )


# ------------------------------------------------------------------------------------>
# Serializers TypeSale


class TypeSaleSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeSale
        fields = (
            'name',
            'description',
        )


# ------------------------------------------------------------------------------------>
# Serializers Sale

class SaleSerializers(serializers.ModelSerializer):
    typeSale = TypeSaleSerializers(many=True)

    class Meta:
        model = Sale
        fields = (
            'idSale',
            'date',
            'typeSale',
        )


# ------------------------------------------------------------------------------------>
# Serializers Bill


class BillSerializers(serializers.ModelSerializer):
    typeBill = TypeBillSerializers(many=True)
    sale = SaleSerializers(many=True)

    class Meta:
        model = Bill
        fields = (
            'idBill',
            'date',
            'subtotal',
            'total',
            'payment',
            'change',
            'typeBill',
            'sale',
        )


# ------------------------------------------------------------------------------------>
# Serializers DetailSale

class DetailSaleSerializers(serializers.ModelSerializer):
    sale = SaleSerializers(many=True)
    branch = StoreSerializers(many=True)
    product = ProductSerializers(many=True)

    class Meta:
        model = DetailSale
        fields = (
            'sale',
            'branch',
            'product',
            'price',
            'quantity',
        )