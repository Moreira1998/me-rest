from rest_framework import viewsets
from apps.store.models import Store
from .serializers import StoreSerializers
from rest_framework import permissions


# ------------------------------------------------------->
# StoreViewSet


class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Store.objects.all()

    def get_serializer_class(self):
        return StoreSerializers


#  ------------------------------------------------------->
#