from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField
from classroom.models import Classroom
from .models import Childcare, ChildcareNews
from website.models import EnrolledChildren, WebsiteNews
from django.contrib.auth.models import User
import autocomplete_light
from utils import autocomplete_light_registry


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


class EnrollmentApplicationForm(ModelForm):
    def __init__(self, childcare_id=None, *args, **kwargs):
        super(EnrollmentApplicationForm, self).__init__(*args, **kwargs)
        self._childcare_id = childcare_id
        self.fields['classroom'] = ModelChoiceField(queryset=Classroom.objects.filter(childcare=self._childcare_id))

    class Meta:
        model = EnrolledChildren
        fields = (
            'classroom',
            'approved',
        )


class EmployeesAddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeesAddForm, self).__init__(*args, **kwargs)
        #self._childcare_id = childcare_id
        self.fields['employees'] = ModelMultipleChoiceField(
            queryset=User.objects.all(),
            widget=autocomplete_light.MultipleChoiceWidget('UserAutocomplete'))

    class Meta:
        model = Childcare
        fields = (
            'employees',
        )


class WebsiteNewsCreateForm(ModelForm):
    class Meta:
        model = WebsiteNews
        fields = ('title',
                  'content',)