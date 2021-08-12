# Django
from django import forms

# Models
from clients.models import Clients, Products


class FormClient(forms.Form):
    first_name = forms.CharField(label='Name', min_length=3, max_length=20)
    last_name = forms.CharField(label='Last Name', min_length=3, max_length=20)
    identification = forms.IntegerField(label='Identification', min_value=1000, max_value=9999999999)


class FormClientCreate(FormClient):

    def clean_identification(self):
        """identification field must be unique"""
        identification = self.cleaned_data['identification']
        identification_exists = Clients.objects.filter(identification=identification).exists()

        if identification_exists:
            raise forms.ValidationError('Already exists a user with this identification registered ')

        return identification


class FormProduct(forms.Form):
    name = forms.CharField(label='Name', min_length=3, max_length=20, )
    price = forms.IntegerField(label='Price')
