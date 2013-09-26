from django import forms
from .models import Childcare, ChildcareNews


class ChildcareCreateForm(forms.ModelForm):
    class Meta:
        model = Childcare
        fields = ('name',
                  'slug',
                  'street_address',
                  'city',
                  'country',)
        #exclude = ('slug',)


class ChildcareNewsCreateForm(forms.ModelForm):
    class Meta:
        model = ChildcareNews
        fields = ('title',
                  'content',)