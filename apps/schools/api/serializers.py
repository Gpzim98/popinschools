from ..models import School

from rest_framework import serializers
from apps.adresses.api.serializers import AddressSerializer


class SchoolSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    logo = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()

    class Meta:
        model = School
        exclude = ['logo_image']

    def get_logo(self, obj):
        return obj.get_image()

    def get_rating(self, obj):
        return obj.ratings

    def get_language(self, obj):
        return obj.language.description
