from rest_framework import viewsets
from apps.staff.models import Staff, Role
from .serializers import StaffSerializers, RoleSerializers
from rest_framework.permissions import IsAuthenticated


#  ------------------------------------------------------->
# ViewSet Staff


class StaffViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Staff.objects.all()

    def get_serializer_class(self):
        return StaffSerializers


#  ------------------------------------------------------->
# ViewSet Role


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Role.objects.all()

    def get_serializer_class(self):
        return RoleSerializers


#  ------------------------------------------------------->

