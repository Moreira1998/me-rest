from rest_framework import viewsets

from rest_framework import permissions

from .serializers import ArrangementSerializers, TypeOrderSerializers, OrderSerializers, ClientSerializers, DetailOrderSerializers

from apps.arrangement.models import Arrangement, TypeOrder, Order, Client, DetailOrder

#  ------------------------------------------------------->
# ViewSet Arrangement


class ArrangementViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Arrangement.objects.all()

    def get_serializer_class(self):
        return ArrangementSerializers

#  ------------------------------------------------------->
# ViewSet TypeOrder


class TypeOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TypeOrder.objects.all()

    def get_serializer_class(self):
        return TypeOrderSerializers


#  ------------------------------------------------------->
# ViewSet TypeOrder


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()

    def get_serializer_class(self):
        return OrderSerializers


#  ------------------------------------------------------->
# ViewSet Client


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()

    def get_serializer_class(self):
        return ClientSerializers


#  ------------------------------------------------------->
# ViewSet Client


class DetailOrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = DetailOrder.objects.all()

    def get_serializer_class(self):
        return DetailOrderSerializers
