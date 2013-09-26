from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from guardian.decorators import permission_required_or_403
from child.forms import ChildCreateForm
from guardian.shortcuts import assign_perm
from django.http import HttpResponseRedirect
from child.models import Child


class ChildCreate(CreateView):
    form_class = ChildCreateForm
    template_name = 'child/child_create.html'

    def form_valid(self, form):
        guardians = form.cleaned_data['guardians']
        obj = form.save(commit=True)
        for user in guardians:
            assign_perm('child_view', user, obj)
            assign_perm('child_update_guardian', user, obj)
        return HttpResponseRedirect(self.get_success_url())


@login_required
@permission_required_or_403('child_view', (Child, 'pk', 'pk'))
def child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    return render(request, 'child/child_detail.html', {'child': child})