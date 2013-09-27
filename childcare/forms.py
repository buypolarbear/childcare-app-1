import autocomplete_light
from utils import autocomplete_light_registry
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField
from .models import Childcare, ChildcareNews, Classroom


class ChildcareCreateForm(ModelForm):
    class Meta:
        model = Childcare
        fields = ('name',
                  'slug',
                  'street_address',
                  'city',
                  'country',)
        #exclude = ('slug',)


class ChildcareNewsCreateForm(ModelForm):
    class Meta:
        model = ChildcareNews
        fields = ('title',
                  'content',)


class ClassroomCreateForm(ModelForm):
    '''using django-autocomplete-light'''
    teachers = ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete_light.MultipleChoiceWidget('UserAutocomplete'))

    class Meta:
        model = Classroom
        fields = (
            'name',
            'description',
            'teachers'
        )