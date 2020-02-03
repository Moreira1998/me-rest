from apps.staff.serializers import UserSerializers


# -------------------------------------------------------->
# jwt_payload_handler


def jwt_payload_handler(user=None, request=None):
    return {
        'user': UserSerializers(user, context={'request': request}).data,
    }

# -------------------------------------------------------->
# jwt_response_payload_handler


def jwt_response_payload_handler(token, user, request):
    return {
        'token': token,
    }

# -------------------------------------------------------->
#