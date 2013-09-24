from django.conf.urls import patterns, url
from childcare import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', views.childcare),
                       url(r'^create/$', views.ChildcareCreate.as_view()),
                       )