from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from guardian.decorators import permission_required_or_403
from guardian.shortcuts import assign_perm
from child.models import Child
from classroom.models import Classroom
from .forms import ChildcareCreateForm, ChildcareNewsCreateForm, EnrollmentApplicationForm, EmployeesAddForm, WebsiteNewsCreateForm
from .models import Childcare, ChildcareNews
from website.models import EnrolledChildren


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
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    childcare_news = ChildcareNews.objects.filter(childcare=childcare)
    classroom_list = Classroom.objects.filter(childcare=childcare)
    return render(request, 'childcare/childcare_detail.html', {'childcare': childcare,
                                                               'news_list': childcare_news,
                                                               'classroom_list': classroom_list})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare_news_create(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = ChildcareNewsCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.childcare = childcare
            obj.save
            form.save(commit=True)
            return HttpResponseRedirect('/childcare/%s' % childcare_id)
    else:
        form = ChildcareNewsCreateForm()
    return render(request, 'childcare/childcare_news_create.html', {'form': form, 'childcare': childcare})


@login_required
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def childcare_news_detail(request, childcare_id, news_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    news = get_object_or_404(ChildcareNews, pk=news_id, childcare=childcare_id)
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
def classrooms_page(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    classroom_list = Classroom.objects.filter(childcare=childcare)
    return render(request, 'childcare/classes_page.html', {'childcare': childcare, 'classroom_list': classroom_list})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def newsboard_page(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    news_list = ChildcareNews.objects.filter(childcare=childcare)
    return render(request, 'childcare/newsboard_page.html', {'childcare': childcare, 'news_list': news_list})


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
def employees_page(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    return render(request, 'childcare/employees_page.html', {'childcare': childcare})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def website_page(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    return render(request, 'childcare/website_page.html', {'childcare': childcare})


@login_required()
@permission_required_or_403('childcare_view', (Childcare, 'pk', 'childcare_id'))
def website_news_create(request, childcare_id):
    childcare = get_object_or_404(Childcare, pk=childcare_id)
    if request.method == 'POST':
        form = WebsiteNewsCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.childcare = childcare
            obj.save
            form.save(commit=True)
            return HttpResponseRedirect('/childcare/%s' % childcare_id)
    else:
        form = WebsiteNewsCreateForm()
    return render(request, 'childcare/website_news_create.html', {'childcare': childcare, 'form': form})