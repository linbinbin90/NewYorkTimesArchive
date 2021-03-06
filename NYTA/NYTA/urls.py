from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView
from NYTArchive import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'NYTA.views.home', name='home'),
                       # url(r'^NYTA/', include('NYTA.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
                       url(r'^geo/$', views.geo, name='geo'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^query/$', views.query, name='query'),
                       url(r'^time_line_query/$', views.time_line_query, name='time_line_query'),
                       url(r'^search/maps/$', views.searchMaps, name='searchMaps'),
                       url(r'^search/location/$', views.searchLocation, name='searchLocation')
)
