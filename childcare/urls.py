from django.conf.urls import patterns, url, include
from childcare import views

urlpatterns = patterns('',
                       #childcare
                       url(r'^(?P<childcare_id>\d+)/$', views.childcare),
                       url(r'^create/$', views.ChildcareCreate.as_view()),
                       url(r'^(?P<childcare_id>\d+)/waiting-list$', views.children_enrollment_list),

                       #newsboard
                       url(r'^(?P<childcare_id>\d+)/news/create/$', views.childcare_news_create),
                       url(r'^(?P<childcare_id>\d+)/news/(?P<news_id>\d+)/$', views.childcare_news_detail),

                       #classroom
                       url(r'^(?P<childcare_id>\d+)/', include('classroom.urls', namespace="classroom")),
                       )