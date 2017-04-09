from django.contrib import admin

from.forms import FormNeighborhood
from .models import (
    Country,
    Region,
    State,
    City,
    Neighborhood,
    Address
)


class StateInline(admin.TabularInline):
    model = State
    extra = 1


class CountryAdmin(admin.ModelAdmin):
    inlines = [
        StateInline,
    ]
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id', 'name')
    search_fields = ('id', 'name')


class CityInline(admin.TabularInline):
    model = City
    extra = 1


class StateAdmin(admin.ModelAdmin):
    inlines = [
        CityInline,
    ]

    list_display = ['id', 'name', 'country', 'region']
    list_filter = ['id', 'name', 'country', 'region']
    ordering = ['id', 'name', 'country', 'region']
    search_fields = ['id', 'name', 'country', 'region']


class NeighborhoodInline(admin.TabularInline):
    model = Neighborhood
    extra = 1


class CityAdmin(admin.ModelAdmin):
    inlines = [
        NeighborhoodInline,
    ]
    list_display = ['id', 'name', 'get_country', 'cep']
    list_filter = ['id', 'name', 'cep']
    ordering = ['id', 'name', 'cep']
    search_fields = ['id', 'name', 'cep']

    def get_country(self, obj):
        return obj.state.country
    get_country.admin_order_field = 'state__country'
    get_country.short_description = 'Pais'


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    ordering = ('id', 'name')
    search_fields = ('id', 'name')


class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'get_state', 'cep')
    list_filter = ('id', 'name', 'city', 'cep')
    ordering = ('id', 'name', 'city', 'cep')
    search_fields = ('id', 'name', 'city', 'cep')
    form = FormNeighborhood

    def get_state(self, obj):
        return obj.city.state
    get_state.admin_order_field = 'city__state'
    get_state.short_description = 'Estado'


class AddresshoodAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'street', 'number', 'neighborhood', 'get_city', 'cep')
    list_filter = ('id', 'street', 'number', 'neighborhood', 'cep')
    ordering = ('id', 'street', 'number', 'neighborhood', 'cep')
    search_fields = ('id', 'street', 'number', 'neighborhood', 'cep')

    def get_city(self, obj):
        return obj.neighborhood.city
    get_city.admin_order_field = 'neighborhood__city'
    get_city.short_description = 'Cidade'


admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Address, AddresshoodAdmin)
