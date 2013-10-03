from django.forms import ModelForm, ModelChoiceField
from classroom.models import Classroom
from .models import Childcare, ChildcareNews
from website.models import EnrolledChildren


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