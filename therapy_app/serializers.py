from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the User model.
    """

    class Meta:
        model = models.User
        fields = ('id', 'email')


class MappingSerializer(serializers.ModelSerializer):
    """
    This serializer will be used to serialize the data of the Mapping model.
    """
    client_email = serializers.EmailField(source='client.email')
    therapist_email = serializers.EmailField(source='therapist.email')

    class Meta:
        model = models.Mapping
        fields = ('id', 'client', 'client_email', 'therapist', 'therapist_email', 'journal_access', 'journal_requested')