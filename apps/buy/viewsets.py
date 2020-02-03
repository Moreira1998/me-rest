from rest_framework import viewsets
from apps.buy.models import Supplier, TypeBuy, Buy, DetailBuy
from .serializers import SupplierSerializers, TypeBuySerializers, BuySerializers, DetailBuySerializers
from rest_framework import permissions


#  ------------------------------------------------------->
# ViewSet Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        return SupplierSerializers


#  ------------------------------------------------------->
# ViewSet TypeBuy


class TypeBuyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TypeBuy.objects.all()

    def get_serializer_class(self):
        return TypeBuySerializers


#  ------------------------------------------------------->
# ViewSet Buy


class BuyViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Buy.objects.all()

    def get_serializer_class(self):
        return BuySerializers


#  ------------------------------------------------------->
# ViewSet Detail


class DetailViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DetailBuy.objects.all()

    def get_serializer_class(self):
        return DetailBuySerializers
