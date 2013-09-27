from django.shortcuts import get_object_or_404, render
from childcare.models import Childcare
from website.models import WebsiteNews


def website(request, childcare_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    return render(request, 'website/childcare_website.html', {'childcare': childcare})


def news_detail(request, childcare_slug, news_slug):
    childcare = get_object_or_404(Childcare, slug=childcare_slug)
    news = get_object_or_404(WebsiteNews, childcare=childcare.pk, slug=news_slug)
    return render(request, 'website/news_detail.html', {'childcare': childcare, 'news': news})