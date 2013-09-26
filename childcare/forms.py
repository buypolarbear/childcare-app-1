from django.forms import ModelForm
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
    class Meta:
        model = Classroom
        fields = (
            'name',
            'description',
        )