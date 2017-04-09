from django.views.generic import ListView, DetailView
from django.conf import settings

from .models import School


class SchoolList(ListView):
    model = School
    template_name = 'schools/school_list.html'

    def get_queryset(self):
        queryset = School.objects.all()
        #
        # import pdb;pdb.set_trace()
        if self.request.GET.get('country'):
            country = self.request.GET.get('country')
            queryset = School.objects.filter(
                address__neighborhood__city__state__country__name=country)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SchoolList, self).get_context_data(**kwargs)
        context['country'] = self.request.GET.get('country')
        return context


class SchoolDetail(DetailView):
    model = School

    def get_context_data(self, **kwargs):
        context = super(SchoolDetail, self).get_context_data(**kwargs)
        context['categories'] = settings.RATINGS_CATEGORIES
        return context
