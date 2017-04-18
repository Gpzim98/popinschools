from django.views.generic import TemplateView
from apps.schools.models import School, Ratings, Profile


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['schools'] = School.objects.all().count()
        context['users'] = Profile.objects.all().count()
        context['ratings'] = Ratings.objects.all().count()
        return context


class AboutUs(TemplateView):
    template_name = 'aboutus.html'
