from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from taskEvents.models import Tasks
from django.urls import reverse_lazy

# Create your views here.

class TaskListView(ListView):
    model = Tasks
class TaskCreateView(CreateView):
    model = Tasks
    fields = '__all__'

class TaskUpdateView(UpdateView):
    model = Tasks
    fields = '__all__'

class TaskDeleteView(DeleteView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task-form')