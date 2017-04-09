from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend
import django_filters
from ..models import School
from .serializers import SchoolSerializer


class SchoolFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(
        name="address__neighborhood__city__state__country__name")
    city = django_filters.CharFilter(
        name="address__neighborhood__city__name")
    language = django_filters.CharFilter(
        name="language__description")

    class Meta:
        model = School
        fields = ['country', 'city', 'language']


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SchoolFilter

    def get_queryset(self):
        queryset = super(SchoolViewSet, self).get_queryset()

        # Filtering by Rating range
        max = int(self.request.GET.get('max_rating'))
        min = int(self.request.GET.get('min_rating'))
        rating_range = range(min, max+1)
        shools_list = [school.id for school in queryset if school.ratings in rating_range]
        queryset = School.objects.filter(id__in=list(set(shools_list)))

        # Filtering by course price
        min_price = int(self.request.GET.get('min_price'))
        max_price = int(self.request.GET.get('max_price'))
        price_range = range(min_price, max_price+1)
        queryset = queryset.filter(course__price__in=price_range)

        # Filtering by visa needed
        visa = True if self.request.GET.get('visa') == 'true' else False
        if visa:
            queryset = queryset.filter(course__visa_needed=visa)

        # Filtering by course type
        class_type = self.request.GET.get('classes_type')
        if class_type:
            queryset = queryset.filter(course__classes_type=class_type)

        # Filtering by shift
        shift = self.request.GET.get('shift')
        if shift:
            queryset = queryset.filter(course__shift=shift)

        return queryset.distinct()
