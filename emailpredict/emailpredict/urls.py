from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'predict.views.index', name='index'),
                       url(r'^verify_email_ajax/',
                           'predict.views.verify_email_ajax', name='verify_email'),
                       url(r'^admin/', include(admin.site.urls), name='admin'),
                       )
