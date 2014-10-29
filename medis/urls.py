from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^tickets/', include('medis.apps.tickets.urls', namespace='tickets')),

    url(r'^admin/', include(admin.site.urls)),
)
