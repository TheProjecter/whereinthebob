from django.conf.urls.defaults import patterns, include, url, handler404
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'witb.bob.views.index'),
    url(r'^directory/$', 'witb.bob.directory.views.index'),
    url(r'^room/(?P<id>\d*)/$', 'witb.bob.room.views.index'),
    url(r'^floor/(?P<id>\d*)/$', 'witb.bob.floor.views.index'),
    url(r'^search/$', 'witb.bob.search.views.index'),
	url(r'^comments/', include('django.contrib.comments.urls')),


    # Examples:
    # url(r'^$', 'witb.views.home', name='home'),
    # url(r'^witb/', include('witb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# handler404 = 'witb.bob.templates.404'
