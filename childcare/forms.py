from django import forms
from childcare.models import Childcare


class ChildcareCreateForm(forms.ModelForm):
    class Meta:
        model = Childcare
        fields = ('name',
                  'slug',
                  'street_address',
                  'city',
                  'country',)