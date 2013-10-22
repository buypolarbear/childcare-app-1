from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from childcare.models import Childcare
from classroom.forms import ClassroomCreateForm, DiaryCreateForm
from classroom.models import Classroom, Diary
from website.models import EnrolledChildren


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def classroom_create(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
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
    return render(request, 'classroom/classroom_create.html', {'form': form, 'childcare': childcare})


@login_required
@permission_required_or_403('classroom_view', (Childcare, 'pk', 'childcare_id'))
def classroom(request, childcare_id, classroom_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    return render(request, 'classroom/classroom_detail.html', {'classroom': classroom, 'childcare': childcare})


@login_required
@permission_required_or_403('classroom_view', (Childcare, 'pk', 'childcare_id'))
def classroom_children_section(request, childcare_id, classroom_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    enrolledchildren_list = EnrolledChildren.objects.filter(childcare=childcare, approved=True, classroom=classroom)
    return render(request, 'classroom/children_section.html', {'classroom': classroom,
                                                            'childcare': childcare,
                                                            'enrolledchildren_list': enrolledchildren_list})


@login_required
@permission_required_or_403('classroom_view', (Childcare, 'pk', 'childcare_id'))
def diary_create(request, childcare_id, classroom_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    if request.method == 'POST':
        form = DiaryCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.classroom = classroom
            obj.author = request.user
            obj.save()
            form.save(commit=True)
            return HttpResponseRedirect('/childcare/%s/classroom/%s/diary' % (childcare_id, classroom_id))
    else:
        form = DiaryCreateForm()
    return render(request, 'classroom/diary_create.html', {'form': form,
                                                           'childcare': childcare,
                                                           'classroom': classroom})


@login_required
@permission_required_or_403('classroom_view', (Childcare, 'pk', 'childcare_id'))
def diary_section(request, childcare_id, classroom_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    diary_list = Diary.objects.filter(classroom=classroom)
    return render(request, 'classroom/diary_section.html', {'classroom': classroom,
                                                            'childcare': childcare,
                                                            'diary_list': diary_list})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def diary_detail(request, childcare_id, classroom_id , diary_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom = get_object_or_404(Classroom, pk=classroom_id)
    diary = get_object_or_404(Diary, pk=diary_id, classroom=classroom)
    return render(request, 'classroom/diary_detail.html', {'classroom': classroom,
                                                                    'childcare': childcare,
                                                                    'diary': diary})