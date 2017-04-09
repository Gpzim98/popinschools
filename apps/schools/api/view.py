from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend
import django_filters
from ..models import School
from .serializers import SchoolSerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()

        # Filtering by language
        language = self.request.GET.get('language')
        if language:
            queryset = queryset.filter(
                language__description__icontains=language)

        # Filtering by city
        city = self.request.GET.get('city')
        if city:
            queryset = queryset.filter(
                address__neighborhood__city__name__icontains=city)

        # Filtering by country
        country = self.request.GET.get('country')
        if country:
            queryset = queryset.filter(
                address__neighborhood__city__state__country__name__icontains=country)

        # Filtering by Rating range
        max = self.request.GET.get('max_rating')
        min = self.request.GET.get('min_rating')

        if max and min:
            rating_range = range(int(min), int(max)+1)
            shools_list = [school.id for school in queryset if school.ratings in rating_range]
            queryset = School.objects.filter(id__in=list(set(shools_list)))

        # Filtering by course price
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if max_price and min_price:
            price_range = range(int(min_price), int(max_price)+1)
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

        return queryset
