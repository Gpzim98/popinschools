from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend
from ..models import School
from .serializers import SchoolSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')
