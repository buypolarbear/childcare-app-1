from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from guardian.decorators import permission_required_or_403
from childcare.forms import ChildcareCreateForm
from childcare.models import Childcare


class ChildcareCreate(CreateView):
    form_class = ChildcareCreateForm
    template_name = 'childcare/childcare_create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.manager = self.request.user
        obj.save
        self.object = obj
        form.save(commit=True)
        childcare = self.object
        manager = self.request.user
        group = Group.objects.get(name='%s: Manager' % childcare.slug)
        manager.groups.add(group)
        return HttpResponseRedirect(self.get_success_url())


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'pk'))
def childcare(request, pk):
    childcare = get_object_or_404(Childcare, pk=pk)
    return render(request, 'childcare/childcare_detail.html', {'childcare': childcare})