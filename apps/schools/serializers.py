from .models import School

from rest_framework import serializers
from apps.adresses.serializers import AddressSerializer


class SchoolSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'

    def get_address(self, obj):
        return AddressSerializer(obj.address)
