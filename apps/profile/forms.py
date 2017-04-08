from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Profile
from ..utils.gender import GENDERS
from ..utils.countries import COUNTRIES


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',
                  'nationality', 'gender', 'birth_day')

    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user.profile.nationality = self.cleaned_data['nationality']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.save()
