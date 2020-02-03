from django.contrib.auth.models import User
from rest_framework import serializers
from apps.staff.models import Staff, Role
from apps.store.serializers import StoreSerializers

# -------------------------------------------------------->
# Serializers Login


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


# -------------------------------------------------------->
# Serializers role


class RoleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


# -------------------------------------------------------->
# Serializers staff


class StaffSerializers(serializers.ModelSerializer):
    store = StoreSerializers(many=True)
    role = RoleSerializers(many=True)

    class Meta:
        model = Staff
        fields = '__all__'


# -------------------------------------------------------->

