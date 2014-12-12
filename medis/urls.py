from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^stats/', include('medis.apps.stats.urls', namespace='stats')),

    url(r'^admin/', include(admin.site.urls)),
)
