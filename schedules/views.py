from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from schedules.models import Shifts
from django.urls import reverse_lazy
# Create your views here.

class ScheduleCreateView(CreateView):
    model = Shifts
    fields = '__all__'
    extra_context = { "shifts": Shifts.objects.all() }
    success_url="/taskmanager/schedules/list/"

class ScheduleListView(ListView):
    model = Shifts

class ScheduleUpdateView(UpdateView):
    model = Shifts
    fields = '__all__'
    success_url = "taskmanager/schedules/create"

def shift_delete(request, pk):
    s = Shifts.objects.get(pk=pk)
    s.delete()
    return redirect("schedues:list")
