from django.conf.urls import patterns, url, include
from childcare import views

urlpatterns = patterns('',
                       #childcare
                       url(r'^(?P<childcare_id>\d+)/$', views.childcare),
                       url(r'^create/$', views.childcare_create),
                       #url(r'^create/$', views.ChildcareCreate.as_view()),

                       #employees
                       url(r'^(?P<childcare_id>\d+)/employees/$', views.employees_section),
                       url(r'^(?P<childcare_id>\d+)/employees/add/$', views.employees_add),

                       #newsboard
                       url(r'^(?P<childcare_id>\d+)/newsboard/$', views.newsboard_section),
                       url(r'^(?P<childcare_id>\d+)/news/create/$', views.childcare_news_create),
                       url(r'^(?P<childcare_id>\d+)/news/(?P<news_id>\d+)/$', views.childcare_news_detail),

                       #classroom
                       url(r'^(?P<childcare_id>\d+)/classrooms/$', views.classrooms_section),
                       url(r'^(?P<childcare_id>\d+)/', include('classroom.urls', namespace="classroom")),

                       #enrollment
                       url(r'^(?P<childcare_id>\d+)/waiting-list/$', views.children_enrollment_list),
                       url(r'^(?P<childcare_id>\d+)/waiting-list/(?P<child_id>\d+)/$', views.child_enrollment_application),

                       #website page
                       url(r'^(?P<childcare_id>\d+)/website/$', views.website_section),
                       url(r'^(?P<childcare_id>\d+)/website/page/create/$', views.website_page_create),
                       url(r'^(?P<childcare_id>\d+)/website/first-page/edit/$', views.website_first_page_edit),
                       url(r'^(?P<childcare_id>\d+)/website/choose-theme/$', views.website_choose_theme),
                       )