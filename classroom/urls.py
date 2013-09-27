from django.conf.urls import patterns, url
from classroom import views

urlpatterns = patterns('',
                       url(r'^classroom/create/$', views.classroom_create),
                       url(r'^classroom/(?P<classroom_id>\d+)/$', views.classroom),
                       )