from rest_framework import serializers

from apps.store.models import Store


# -------------------------------------------------------->
# Serializers Store


class StoreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = (
            'store',
            'branch',
            'direction',
            'phone',
            'phone2',
            'email',
        )


# -------------------------------------------------------->

