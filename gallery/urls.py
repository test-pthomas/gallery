from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gallery.views.home', name='home'),
    url(r'^my-galleries/$', 'gallery.views.my_galleries', name='my_galleries'),
    url(r'^create-gallery/$', 'gallery.views.create', name='create'),
    url(r'^gallery-list/$', 'gallery.views.gallery_list', name='gallery_list'),
    url(r'^login/$', 'gallery.views.login', name='login'),
    url(r'^logout/$', 'gallery.views.logout', name='logout'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)