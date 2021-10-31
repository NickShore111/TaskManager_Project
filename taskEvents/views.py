from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from taskEvents.models import Tasks
from employees.models import Positions

# Create your views here.

class TaskListView(ListView):
    frequencies = dict()
    model = Tasks
    for key, value in Tasks.TaskFrequency.choices:
        frequencies[key] = value

    extra_context = {
        "positions": Positions.objects.all(),
        "frequencies": frequencies,
    }
class TaskCreateView(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = '/taskmanager/tasks/create/'
class TaskUpdateView(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = '/taskmanager/tasks/list/'

def delete_task(request, pk):
    t = Tasks.objects.get(pk=pk)
    t.delete()
    return redirect("tasks:list")

def task_select(request):
    frequencies = dict()
    for key, value in Tasks.TaskFrequency.choices:
        frequencies[key] = value

    if request.method == "POST":
        if request.POST['position']:
            results = Tasks.objects.filter(position_id = request.POST['position'])
    
        if request.POST['frequency']:
            results = Tasks.objects.filter(frequency = request.POST['frequency'])

    if request.method == "GET":
        results = Tasks.objects.all()

    context = {
        "positions": Positions.objects.all(),
        "frequencies": frequencies,
        "object_list": results,
    }
    return render(request, "taskEvents/tasks_list.html", context)