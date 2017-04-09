from rest_framework import serializers

from ..models import Address, City, Neighborhood, State, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

    country = CountrySerializer()


class CitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    state = StateSerializer()


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'
    city = CitySerialzer()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    neighborhood = NeighborhoodSerializer()
