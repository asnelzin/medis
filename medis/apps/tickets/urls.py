from django.conf.urls import patterns, url

from medis.apps.tickets.views import MonthStatsView, AjaxTicketsList

urlpatterns = patterns(
    '',
    url(r'^month_stats/$', MonthStatsView.as_view(), name='month_stats'),
    url(r'^month_stats/ajax/$', AjaxTicketsList.as_view(), name='month_stats_ajax'),

)