from django.conf.urls import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^stats/', include('medis.apps.stats.urls', namespace='stats')),

    url(r'^admin/', include(admin.site.urls)),
)
