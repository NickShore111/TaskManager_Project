from django.http.request import HttpRequest
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from schedules.models import Shifts, Schedule
from django.urls import reverse_lazy
from schedules.forms import ScheduleForm, ShiftForm

from django.forms import inlineformset_factory, modelform_factory
# Create your views here.

class ShiftCreateView(CreateView):
    model = Shifts
    fields = '__all__'
    extra_context = { "shifts": Shifts.objects.all() }
    success_url="/taskmanager/schedules/list/"

class ShiftListView(ListView):
    model = Shifts

class ShiftUpdateView(UpdateView):
    model = Shifts
    fields = '__all__'
    success_url = "taskmanager/schedules/create"

def shift_delete(request, pk):
    s = Shifts.objects.get(pk=pk)
    s.delete()
    return redirect("schedues:list")

def schedule_select(request):
    schedules = Schedule.objects.all()
    scheduleForm = ScheduleForm()
    context = {
        "schedules": schedules,
        "scheduleForm": scheduleForm
    }
    return render(request, "schedules/shifts_list.html", context)

def schedule_form(request):
    shiftsForm = ShiftForm()
    scheduleForm = ScheduleForm()
    context = {
        "shiftsForm": shiftsForm,
        "scheduleForm": scheduleForm,
    }
    return render(request, "schedules/shifts_form.html", context)

def create_schedule(request):

    form = ScheduleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("select/")

    else:
        schedules = Schedule.objects.all()

        print(form.errors)
        context = { 
            "scheduleForm": form,
            "schedules": schedules,
            
        }
        return render(request, "schedules/shifts_list.html", context)

def select_schedule(request):
    shifts = Shifts.objects.filter(date_id= request.POST['date'])
    context = {
        "object_list": shifts
    }
    return render(request, "schedules/shifts_list.html", context)
