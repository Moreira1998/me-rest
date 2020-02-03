from rest_framework import viewsets

from apps.product.models import Category, Brand, State, Price, Product

from .serializers import CategorySerializers, BrandSerializers, StateSerializers
from .serializers import PriceSerializers, ProductSerializers

from rest_framework.permissions import IsAuthenticated


#  ------------------------------------------------------->
# ViewSet Category


class CategoryViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return CategorySerializers


#  ------------------------------------------------------->
# ViewSet Brand


class BrandViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        return BrandSerializers


#  ------------------------------------------------------->
# ViewSet State


class StateViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = State.objects.all()

    def get_serializer_class(self):
        return StateSerializers


#  ------------------------------------------------------->
# ViewSet Price


class PriceViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Price.objects.all()

    def get_serializer_class(self):
        return PriceSerializers


#  ------------------------------------------------------->
# ViewSet Product


class ProductViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()

    def get_serializer_class(self):
        return ProductSerializers


