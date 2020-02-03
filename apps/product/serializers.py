from rest_framework import serializers
from apps.product.models import Category, Brand, State, Price, Product


# -------------------------------------------------------->
# Serializers Category


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )


# -------------------------------------------------------->
# Serializers Brand


class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = (
            'name',
            'description',
        )


# -------------------------------------------------------->
# Serializers State


class StateSerializers(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = (
            'name',
            'description',
        )


# -------------------------------------------------------->
# Serializers Price


class PriceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = (
            'purchasePrice',
            'salePrice',
        )


# -------------------------------------------------------->
# Serializers Product


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers(many=True)
    brand = BrandSerializers(many=True)
    state = StateSerializers(many=True)
    price = PriceSerializers(many=True)

    class Meta:
        model = Product
        fields = (
            'idProduct',
            'name',
            'category',
            'brand',
            'state',
            'price',

        )


