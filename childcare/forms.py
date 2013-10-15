from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField
from classroom.models import Classroom
from .models import Childcare, News
from website.models import EnrolledChildren, Page
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


class NewsCreateForm(ModelForm):
    class Meta:
        model = News
        fields = ('title',
                  'content',
                  'public',)


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
        self.fields['employees'] = ModelMultipleChoiceField(
            queryset=User.objects.all(),
            widget=autocomplete_light.MultipleChoiceWidget('UserAutocomplete'))

    class Meta:
        model = Childcare
        fields = (
            'employees',
        )


class FirstPageForm(ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super(FirstPageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Childcare
        fields = (
            'description',
        )


class WebsitePageCreateForm(ModelForm):
    class Meta:
        model = Page
        fields = ('title',
                  'content',
                  'order',)