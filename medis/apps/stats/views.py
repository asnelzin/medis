# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.views.generic import TemplateView

from medis.apps.stats.forms import FilterForm
from medis.apps.stats.models import Speciality, Ticket


class MonthStatsView(TemplateView):
    template_name = 'stats/month.html'

    def get_form_errors(self, form):
        return dict([(k, [unicode(e) for e in v]) for k, v in form.errors.items()])

    def data_to_json(self, context_dict):
        return json.dumps(context_dict, cls=DjangoJSONEncoder)

    def get_context_data(self, **kwargs):
        context = super(MonthStatsView, self).get_context_data(**kwargs)
        current_date = datetime.now()
        data = Ticket.objects.get_monthly_stats(current_date.month, current_date.year)
        context['form'] = self.form
        context['current_date'] = current_date
        context['data'] = data
        return context

    def get_json_response(self):
        if self.form.is_valid():
            data = Ticket.objects.get_monthly_stats(self.form.data['month'], self.form.data['year'])
            return HttpResponse(self.data_to_json(data), content_type='application/json')
        json_content = self.data_to_json(self.get_form_errors(self.form))
        return HttpResponse(json_content, content_type='application/json', status=400)

    def get(self, request, *args, **kwargs):
        self.form = FilterForm(request.GET)
        if self.request.is_ajax():
            return self.get_json_response()
        context = self.get_context_data()
        return self.render_to_response(context)


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
