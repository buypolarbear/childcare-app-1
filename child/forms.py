import autocomplete_light
from utils import autocomplete_light_registry
from django import forms
from django.contrib.auth.models import User
from .models import Child

__author__ = 'matej'


class ChildCreateForm(forms.ModelForm):
    '''using django-autocomplete-light'''
    guardians = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete_light.MultipleChoiceWidget('UserAutocomplete'))

    class Meta:
        model = Child
        exclude = (
            'information',
            'teacher_notes',
        )