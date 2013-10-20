import autocomplete_light
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

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

    #childcare
    url(r'^childcare/', include('childcare.urls', namespace="childcare")),

    #child
    url(r'^children/', include('child.urls', namespace="child")),

    #website
    url(r'^(?P<childcare_slug>[\w\-]+)/', include('website.urls', namespace="website")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)