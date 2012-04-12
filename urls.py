from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'galleria.views.home', name='home'),
    url(r'^my-galleries/$', 'galleria.views.my_galleries', name='my_galleries'),
    url(r'^my-galleries/add-image/$', 'galleria.views.add_image', name='add_image'),
    url(r'^create-gallery/$', 'galleria.views.create', name='create_gallery'),
    url(r'^gallery-list/$', 'galleria.views.gallery_list', name='gallery_list'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'logout.html'}, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)