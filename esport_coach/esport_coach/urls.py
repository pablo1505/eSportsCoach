"""esport_tutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from sideapp import views


urlpatterns = [

    url(r'^$', 'sideapp.views.home', name='home'),
    url(r'^contact/', 'sideapp.views.contact', name='contact'),
    url(r'^signup/', 'sideapp.views.signup', name='signup'),
    url(r'^findcoach/', 'sideapp.views.findcoach', name='findcoach'),
    url(r'^list_of_coaches/', 'sideapp.views.list_of_coaches', name='list_of_coaches'),
    url(r'^tutorselected/(?P<tutor_id>[0-9]+)', 'sideapp.views.tutorselected', name='tutorselected'),
    url(r'^paymentpage/', 'sideapp.views.paymentpage', name='paymentpage'),
    url(r'^streampage/', 'sideapp.views.streampage', name='streampage'),
    
    url(r'^charge/$', 'sideapp.views.charge', name="charge"),
    
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
