from django.views.generic import ListView, DetailView, FormView
from django.conf import settings
from django.shortcuts import resolve_url, redirect, HttpResponseRedirect

from .models import School, Comment, AlreadyStudiedHere
from .forms import CommentForm


class SchoolList(ListView):
    model = School
    template_name = 'schools/school_list.html'

    def get_queryset(self):
        queryset = School.objects.all()

        if self.request.GET.get('country'):
            country = self.request.GET.get('country')
            queryset = School.objects.filter(
                address__neighborhood__city__state__country__name__icontains=country)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SchoolList, self).get_context_data(**kwargs)
        context['country'] = self.request.GET.get('country', '')
        return context


class SchoolDetail(DetailView):
    model = School

    def get_context_data(self, **kwargs):
        context = super(SchoolDetail, self).get_context_data(**kwargs)
        context['categories'] = settings.RATINGS_CATEGORIES

        if self.request.user.is_authenticated:
            form = CommentForm(
                instance=Comment(
                    school=self.object, user=self.request.user.profile
                )
            )
            context['form'] = form

            ash = AlreadyStudiedHere.objects.filter(
                school=self.object, user=self.request.user.profile)
            context['already_studied_here'] = ash
        context['comments'] = Comment.objects.filter(
            school=self.get_object(), approved=True)
        return context


class SchoolComment(FormView):
    form_class = CommentForm

    def get_success_url(self):
        return resolve_url('schools:school-profile', self.kwargs.get('pk'))

    def form_valid(self, form):
        form.save()
        return super(SchoolComment, self).form_valid(form)


def already_studied_here(request, pk):
    if request.user.is_authenticated:
        school = School.objects.get(pk=pk)
        ash = AlreadyStudiedHere.objects.filter(school=school,
                                                user=request.user.profile)
        if ash:
            ash.delete()
        else:
            AlreadyStudiedHere.objects.create(
                school=school, user=request.user.profile)

        return redirect('schools:school-profile', pk)
    else:
        return HttpResponseRedirect('/accounts/login/?next=/schools/profile/1/')

