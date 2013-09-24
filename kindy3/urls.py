from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^kindy3/', include('kindy3.foo.urls')),

    # home
    url(r'^$', 'kindy3.views.home', name='home'),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # registration
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^childcare/', include('childcare.urls', namespace="childcare")),
)
