from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from childcare.models import Childcare
from classroom.forms import ClassroomCreateForm
from classroom.models import Classroom


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def classroom_create(request, childcare_id):
    if request.method == 'POST':
        childcare = get_object_or_404(Childcare, pk=childcare_id)
        form = ClassroomCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.childcare = childcare
            teachers = form.cleaned_data['teachers']
            obj.save()
            form.save(commit=True)
            for teacher in teachers:
                assign_perm('classroom_view', teacher, childcare)
            return HttpResponseRedirect('/childcare/%s' % childcare_id)
    else:
        form = ClassroomCreateForm()
    return render(request, 'childcare/classroom_create.html', {'form': form})


@login_required
@permission_required_or_403('classroom_view', (Childcare, 'pk', 'childcare_id'))
def classroom(request, childcare_id, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    return render(request, 'childcare/classroom_detail.html', {'classroom': classroom})