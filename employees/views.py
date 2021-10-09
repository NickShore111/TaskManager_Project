from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.


def index(request):
    employeeForm = EmployeeForm()
    context = {"employeeForm": employeeForm}
    return render(request, "employees/base_employees.html", context)
