from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from childcare.models import Childcare
from website.forms import EnrollChildForm
from website.models import WebsiteNews


def website(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    return render(request, 'website/childcare_website.html', {'childcare': childcare})


def news_detail(request, childcare_slug, news_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    news = get_object_or_404(WebsiteNews, childcare=childcare.pk, slug=news_slug)
    return render(request, 'website/news_detail.html', {'childcare': childcare, 'news': news})


@login_required
def enroll_child(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    #TODO
    if request.method == 'POST':
        form = EnrollChildForm(request.user, request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.childcare = childcare
            obj.save()
            form.save(commit=True)
            return HttpResponseRedirect('/%s/enrollment-sent' % childcare_slug)
    else:
        form = EnrollChildForm(request.user)
    return render(request, 'website/enroll_child.html', {'form': form})


def enroll_child_confirmation(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    return render(request, 'website/enroll_child_confirmation.html', {'childcare': childcare})