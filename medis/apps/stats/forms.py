import calendar
from datetime import datetime

from django import forms


class FilterForm(forms.Form):
    MONTH_CHOICES = tuple((idx, name) for idx, name in enumerate(calendar.month_name[1:], start=1))
    YEAR_CHOICES = tuple((n, str(n)) for n in range(2010, datetime.now().year + 1))
    month = forms.ChoiceField(choices=MONTH_CHOICES, initial=datetime.now().month)
    year = forms.ChoiceField(choices=YEAR_CHOICES, initial=datetime.now().year)
