from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from childcare.models import Childcare, News
from website.forms import EnrollChildForm
from website.models import Page


def website(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    #website_news_list = News.objects.filter(childcare=childcare, public=True)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    return render(request, 'website/website_home.html', {'childcare': childcare,
                                                         #'news_list': website_news_list,
                                                         'pages_list': pages_list,
                                                         'theme_path': theme_path})


def website_news(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    website_news_list = News.objects.filter(childcare=childcare, public=True)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    return render(request, 'website/website_news.html', {'childcare': childcare,
                                                         'news_list': website_news_list,
                                                         'pages_list': pages_list,
                                                         'theme_path': theme_path})


def news_detail(request, childcare_slug, news_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    news = get_object_or_404(News, childcare=childcare.pk, slug=news_slug)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    return render(request, 'website/news_detail.html', {'childcare': childcare,
                                                        'news': news,
                                                        'pages_list': pages_list,
                                                        'theme_path': theme_path})


@login_required
def enroll_child(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    #TODO
    if request.method == 'POST':
        form = EnrollChildForm(request.user, request.POST)
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.childcare = childcare
                obj.save()
                form.save(commit=True)
                return HttpResponseRedirect('/%s/enrollment-sent' % childcare_slug)
            except:
                return HttpResponse("The enrollment application for your child has already been sent.")
    else:
        form = EnrollChildForm(request.user)
    return render(request, 'website/enroll_child.html', {'form': form,
                                                         'childcare': childcare,
                                                         'pages_list': pages_list,
                                                         'theme_path': theme_path})


def enroll_child_confirmation(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    return render(request, 'website/enroll_child_confirmation.html', {'childcare': childcare,
                                                                      'pages_list': pages_list,
                                                                      'theme_path': theme_path})


def page_detail(request, childcare_slug, page_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    page = get_object_or_404(Page, childcare=childcare.pk, slug=page_slug)
    pages_list = Page.objects.filter(childcare=childcare)
    theme_path = 'themes/'+childcare.theme+'.html'
    return render(request, 'website/page_detail.html', {'childcare': childcare,
                                                        'page': page,
                                                        'pages_list': pages_list,
                                                        'theme_path': theme_path})