import autocomplete_light
import datetime
from django.forms.extras.widgets import SelectDateWidget
from child.models import Child
from classroom.models import Classroom, Diary, Attendance
from utils import autocomplete_light_registry
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelMultipleChoiceField, DateField, CheckboxSelectMultiple
from website.models import EnrolledChild


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
    date = DateField(widget=SelectDateWidget, initial=datetime.date.today)

    class Meta:
        model = Diary
        fields = (
            'date',
            'content',
        )


class AttendanceCreateForm(ModelForm):
    def __init__(self, classroom=None, *args, **kwargs):
        super(AttendanceCreateForm, self).__init__(*args, **kwargs)
        enrolled = EnrolledChild.objects.filter(classroom=classroom, approved=True)
        children_ids = []
        for object in enrolled:
            children_ids.append(object.child.pk)
        self.fields['attendance'] = ModelMultipleChoiceField(queryset=Child.objects.filter(id__in=children_ids),
                                                             widget=CheckboxSelectMultiple(attrs={"checked":""}),
                                                             required=True)

    date = DateField(widget=SelectDateWidget, initial=datetime.date.today)

    class Meta:
        model = Attendance
        fields = (
            'date',
            'attendance',
        )