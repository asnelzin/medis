# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, View

from medis.apps.stats.forms import FilterForm
from medis.apps.stats.models import Speciality, Ticket


class AjaxMonthStatsView(View):
    def get_form_errors(self, form):
        return dict([(k, [unicode(e) for e in v]) for k, v in form.errors.items()])

    def data_to_json(self, context_dict):
        return json.dumps(context_dict, cls=DjangoJSONEncoder)

    def render_json_response(self, json_context='', status=200):
        return HttpResponse(json_context, content_type='application/json', status=status)

    def render_form_error_json_response(self, form, status=400):
        json_context = self.data_to_json(self.get_form_errors(form))
        return HttpResponse(json_context, content_type='application/json', status=status)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = FilterForm(request.POST)
            if form.is_valid():
                data = Ticket.objects.get_monthly_stats(form.data['month'], form.data['year'])
                return self.render_json_response(self.data_to_json(data))
            else:
                return self.render_form_error_json_response(form)
        else:
            return self.render_json_response('', 404)


class MonthStatsView(FormView):
    form_class = FilterForm
    template_name = 'stats/month.html'

    def get_context_data(self, **kwargs):
        context = super(MonthStatsView, self).get_context_data(**kwargs)

        current_date = datetime.now()
        data = Ticket.objects.get_monthly_stats(current_date.month, current_date.year)
        context.update({
            'current_date': current_date,
            'data': data
        })
        return context


class SpecialityStatsView(TemplateView):
    template_name = 'stats/speciality.html'

    def get(self, request, *args, **kwargs):
        speciality = Speciality.objects.get_or_none(pk=request.GET.get('speciality'))
        form = FilterForm(request.GET)
        if form.is_valid() and speciality:
            context = super(SpecialityStatsView, self).get_context_data(**kwargs)
            data = Ticket.objects.get_speciality_stats(speciality, request.GET['month'], request.GET['year'])
            context.update({
                'speciality_name': speciality.name,
                'data': data
            })
            return self.render_to_response(context)
        else:
            return HttpResponse('Bad Request', status=400)
