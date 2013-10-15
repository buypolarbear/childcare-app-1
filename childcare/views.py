from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required_or_403
from child.models import Child
from classroom.models import Classroom
from .forms import ChildcareCreateForm, NewsCreateForm, EnrollmentApplicationForm, EmployeesAddForm, WebsitePageCreateForm, FirstPageForm
from .models import Childcare, News
from website.models import EnrolledChildren, Page


@login_required
def childcare_create(request):
    if request.method == 'POST':
        form = ChildcareCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.manager = request.user
            obj.save
            object = obj
            form.save(commit=True)
            childcare = object
            manager = request.user
            group = Group.objects.get(name='%s: Manager' % childcare.slug)
            manager.groups.add(group)
            return HttpResponseRedirect('/home')
    else:
        form = ChildcareCreateForm()
    return render(request, 'childcare/childcare_create.html', {'form': form})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    childcare_news = News.objects.filter(childcare=childcare)
    classroom_list = Classroom.objects.filter(childcare=childcare)
    return render(request, 'childcare/childcare_detail.html', {'childcare': childcare,
                                                               'news_list': childcare_news,
                                                               'classroom_list': classroom_list})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare_news_create(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = NewsCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.childcare = childcare
            obj.save()
            form.save(commit=True)
            return HttpResponseRedirect('/childcare/%s' % childcare_id)
    else:
        form = NewsCreateForm()
    return render(request, 'childcare/childcare_news_create.html', {'form': form, 'childcare': childcare})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare_news_detail(request, childcare_id, news_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    news = get_object_or_404(News, pk=news_id, childcare=childcare_id)
    return render(request, 'childcare/childcare_news_detail.html', {'childcare': childcare, 'news': news})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def children_enrollment_list(request, childcare_id):
    #waiting list
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    enrollment_list = EnrolledChildren.objects.filter(childcare=childcare, approved=False)
    return render(request,
                  'childcare/childcare_enrollment_list.html',
                  {'childcare': childcare, 'enrollment_list': enrollment_list})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def child_enrollment_application(request, childcare_id, child_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    child = get_object_or_404(Child, pk=child_id)
    application = get_object_or_404(EnrolledChildren, child=child, childcare=childcare_id)
    if request.method == 'POST':
        form = EnrollmentApplicationForm(childcare, request.POST, instance=application)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/childcare/%s/waiting-list' % childcare_id)
    else:
        form = EnrollmentApplicationForm(childcare, instance=application)
    return render(request,
                  'childcare/child_enrollment_application.html',
                  {'childcare': childcare, 'application': application, 'form': form})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def classrooms_section(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom_list = Classroom.objects.filter(childcare=childcare)
    return render(request, 'childcare/classes_section.html', {'childcare': childcare, 'classroom_list': classroom_list})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def newsboard_section(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    news_list = News.objects.filter(childcare=childcare)
    return render(request, 'childcare/newsboard_section.html', {'childcare': childcare, 'news_list': news_list})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def employees_add(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = EmployeesAddForm(request.POST, instance=childcare)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/childcare/%s/employees' % childcare_id)
    else:
        form = EmployeesAddForm(instance=childcare)
    return render(request, 'childcare/employees_add.html', {'form': form, 'childcare': childcare})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def employees_section(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    return render(request, 'childcare/employees_section.html', {'childcare': childcare})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def website_section(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    website_news_list = News.objects.filter(childcare=childcare, public=True)
    pages_list = Page.objects.filter(childcare=childcare)
    return render(request, 'childcare/website_section.html', {'childcare': childcare,
                                                           'website_news_list': website_news_list,
                                                           'pages_list': pages_list})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def website_page_create(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = WebsitePageCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.childcare = childcare
            obj.save
            form.save(commit=True)
            return HttpResponseRedirect('/childcare/%s/website' % childcare_id)
    else:
        form = WebsitePageCreateForm()
    return render(request, 'childcare/website_page_create.html', {'form': form, 'childcare': childcare})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def website_first_page_edit(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = FirstPageForm(request.POST, instance=childcare)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/childcare/%s/website' % childcare_id)
    else:
        form = FirstPageForm(instance=childcare)
    return render(request, 'childcare/first_page_edit.html', {'form': form, 'childcare': childcare})