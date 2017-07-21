from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    usernumber = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True, max_length=100)
