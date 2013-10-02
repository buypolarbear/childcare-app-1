from django.forms import ModelForm, ModelChoiceField
from child.models import Child
from website.models import EnrolledChildren


class EnrollChildForm(ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super(EnrollChildForm, self).__init__(*args, **kwargs)
        self._user = user
        self.fields['child'] = ModelChoiceField(queryset=Child.objects.filter(guardians__id=self._user.pk))

    class Meta:
        model = EnrolledChildren
        fields = (
            'child',
        )