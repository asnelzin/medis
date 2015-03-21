from django.conf.urls import patterns, url

from medis.apps.stats.views import (AjaxMonthStatsView, MonthStatsView,
                                    SpecialityStatsView)

urlpatterns = patterns(
    '',
    url(r'^month/$', MonthStatsView.as_view(), name='month'),
    url(r'^month/ajax/$', AjaxMonthStatsView.as_view(), name='month-ajax'),
    url(r'^spec/', SpecialityStatsView.as_view(), name='month-speciality'),
)
