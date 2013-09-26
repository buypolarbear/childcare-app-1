from django.conf.urls import patterns, url
from child import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', views.child),
                       url(r'^create/$', views.ChildCreate.as_view()),
                       #url(r'^(?P<pk>\d+)/news/create/$', views.create_childcare_news),
                       )