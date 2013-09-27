import autocomplete_light
from classroom.models import Classroom
from utils import autocomplete_light_registry
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField


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