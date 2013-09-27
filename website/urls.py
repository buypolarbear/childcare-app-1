from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
                       url(r'^$', views.website),
                       url(r'^news/(?P<news_slug>[\w\-]+)/$', views.news_detail),
                       )