from django.conf.urls import patterns, url
from childcare import views

urlpatterns = patterns('',
                       #childcare
                       url(r'^(?P<pk>\d+)/$', views.childcare),
                       url(r'^create/$', views.ChildcareCreate.as_view()),

                       #newsboard
                       url(r'^(?P<pk>\d+)/news/create/$', views.childcare_news_create),
                       url(r'^(?P<childcare_id>\d+)/news/(?P<news_id>\d+)/$', views.childcare_news_detail),

                       #classroom
                       url(r'^(?P<childcare_id>\d+)/classroom/create/$', views.classroom_create),
                       url(r'^(?P<childcare_id>\d+)/classroom/(?P<classroom_id>\d+)/$', views.classroom),
                       )