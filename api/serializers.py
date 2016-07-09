from rest_framework import serializers

from api.models import (
    SignUp
)


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp


