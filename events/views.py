# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
import datetime
import calendar
from django.utils.safestring import mark_safe
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from events.models import Events
from .utils import EventCalendar
from events.forms import EventForm
# Depricated for EventsCalendar
# from calendar import HTMLCalendar

class EventListView(ListView):
    model = Events

class EventFormView(FormView):
    form_class = EventForm
    template_name = 'events/events_form.html'
    success_url = '/taskmanager/events/'

class EventCreateView(CreateView):
    model = Events
    fields = '__all__'
    success_url="/taskmanager/events/list/"

class EventUpdateView(UpdateView):
    model = Events
    fields = '__all__'
    # template_name = 'events/events_update.html'
    # success_url="/taskmanager/list/"


# class EventDeleteView(DeleteView):
#     model = Events
#     fields = '__all__'

def delete_event(request, pk):
    e = Events.objects.get(pk=pk)
    e.delete()
    return redirect("events:list")

def calendar_view(request, extra_context=None):
    after_day = request.GET.get('day__gte', None)
    extra_context = extra_context or {}

    if not after_day:
        d = datetime.date.today()
    else:
        try:
            split_after_day = after_day.split('-')
            d = datetime.date(year=int(split_after_day[0]), month=int(
                split_after_day[1]), day=1)
        except:
            d = datetime.date.today()

    # find first day of current month
    previous_month = datetime.date(year=d.year, month=d.month, day=1)
    previous_month = previous_month - \
        datetime.timedelta(days=1)  # backs up a single day
    # find first day of previous month
    previous_month = datetime.date(
        year=previous_month.year, month=previous_month.month, day=1)

    last_day = calendar.monthrange(d.year, d.month)
    # find last day of current month
    next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
    next_month = next_month + \
        datetime.timedelta(days=1)  # forward a single day
    # find first day of next month
    next_month = datetime.date(
        year=next_month.year, month=next_month.month, day=1)

    extra_context['previous_month'] = "/taskmanager/events/" + '?day__gte=' + str(
        previous_month)
    extra_context['next_month'] = "/taskmanager/events/" + \
        '?day__gte=' + str(next_month)

    cal = EventCalendar()
    # cal = HTMLCalendar()
    html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
    html_calendar = html_calendar.replace(
        '<td ', '<td  width="150" height="80" id="cal_cell"')
    extra_context['calendar'] = mark_safe(html_calendar)
    # print("Extra Content: ", extra_context)

    return render(request, 'events/base_calendar.html', extra_context)


