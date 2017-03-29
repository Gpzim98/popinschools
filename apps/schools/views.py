from django.views.generic import ListView, DetailView
from django.conf import settings

from .models import School


class SchoolList(ListView):
    model = School
    queryset = School.objects.all()


class SchoolDetail(DetailView):
    model = School

    def get_context_data(self, **kwargs):
        context = super(SchoolDetail, self).get_context_data(**kwargs)
        context['categories'] = settings.RATINGS_CATEGORIES
        return context
