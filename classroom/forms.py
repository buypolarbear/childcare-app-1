import autocomplete_light
from django.forms.extras.widgets import SelectDateWidget
from classroom.models import Classroom, Diary
from utils import autocomplete_light_registry
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, DateField


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
            'teachers',
        )


class DiaryCreateForm(ModelForm):
    created = DateField(widget=SelectDateWidget, label='Date')

    class Meta:
        model = Diary
        fields = (
            'created',
            'content',
        )