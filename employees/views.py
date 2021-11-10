from django.shortcuts import (
    render,
    redirect,
)
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employees
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy

# Create your views here.

class EmployeeListView(ListView):
    """Shows a list of all employees in a table"""
    model = Employees


class ActiveEmployeeListView(ListView):
    """Shows a list of all Active employees in a table"""
    model = Employees
    queryset = Employees.objects.filter(status=1)

class EmployeeFormView(FormView):
    """New employee form """
    template_name = 'employees/employees_form.html'
    form_class = EmployeeForm
    model = Employees
    

class EmployeeCreateView(CreateView):
    model = Employees
    fields = '__all__'
    success_url = reverse_lazy('employees:list')

class EmployeeUpdateView(UpdateView):
    
    template_name = 'employees/employees_update.html'
    model = Employees
    fields = '__all__'
    success_url = reverse_lazy('employees:list')
    
class EmployeeDeleteView(DeleteView):
    model = Employees
    fields = '__all__'
    success_url = reverse_lazy('employees:list')
