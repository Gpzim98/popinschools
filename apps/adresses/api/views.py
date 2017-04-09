from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import AddressSerializer
from rest_framework.viewsets import ModelViewSet
from ..models import Address


class PeopleViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    http_method_names = ['get']
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id', 'description', 'user']
