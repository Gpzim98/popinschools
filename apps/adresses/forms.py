from localflavor.br.forms import BRZipCodeField
from django import forms

from .models import Neighborhood


class FormNeighborhood(forms.ModelForm):
    cep = BRZipCodeField(label='CEP')

    class Meta:
        model = Neighborhood
        fields = '__all__'
