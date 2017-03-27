from django.views.generic import ListView

from .models import School


class SchoolList(ListView):
    model = School
    queryset = School.objects.all()

