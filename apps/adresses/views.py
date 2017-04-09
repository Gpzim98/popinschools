from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    '''
        Endpoint used to create, update and retrieve addreses
        Allow: GET, POST, UPDATE, OPTIONS
    '''
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get', 'options']
