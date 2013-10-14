from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
                       url(r'^$', views.website),
                       url(r'^news/(?P<news_slug>[\w\-]+)/$', views.news_detail),
                       url(r'^enroll$', views.enroll_child),
                       url(r'^enrollment-sent$', views.enroll_child_confirmation),
                       url(r'^(?P<page_slug>[\w\-]+)/$', views.page_detail),
                       )