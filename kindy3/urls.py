import autocomplete_light
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
autocomplete_light.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^kindy3/', include('kindy3.foo.urls')),

    url(r'^$', 'kindy3.views.main', name='main'),
    url(r'^home/$', 'kindy3.views.home', name='home'),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #autocomplete
    url(r'autocomplete/', include('autocomplete_light.urls')),

    # registration
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^childcare/', include('childcare.urls', namespace="childcare")),
    url(r'^children/', include('child.urls', namespace="child")),
)
