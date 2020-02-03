from rest_framework import viewsets
from apps.sale.models import TypeBill, TypeSale, Bill, Sale, DetailSale
from apps.sale.serializers import TypeBillSerializers, TypeSaleSerializers, BillSerializers, SaleSerializers, DetailSaleSerializers
from rest_framework import permissions

#  ------------------------------------------------------->
# ViewSet TypeBill


class TypeBillViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TypeBill.objects.all()

    def get_serializer_class(self):
        return TypeBillSerializers

#  ------------------------------------------------------->
# ViewSet TypeSale


class TypeSaleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TypeSale.objects.all()

    def get_serializer_class(self):
        return TypeSaleSerializers


#  ------------------------------------------------------->
# ViewSet Bill


class BillViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Bill.objects.all()

    def get_serializer_class(self):
        return BillSerializers


#  ------------------------------------------------------->
# ViewSet Sale


class SaleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sale.objects.all()

    def get_serializer_class(self):
        return SaleSerializers

#  ------------------------------------------------------->
# ViewSet DetailSale


class DetailSaleViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DetailSale.objects.all()

    def get_serializer_class(self):
        return DetailSaleSerializers
