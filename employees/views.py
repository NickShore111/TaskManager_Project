from django.http.response import HttpResponseRedirect
from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
    reverse,
)
from django.contrib import messages
from .forms import EmployeeForm

# Create your views here.


def index(request):
    employeeForm = EmployeeForm()
    context = {"employeeForm": employeeForm}
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            newEmployee = form.save(commit=False)
            newEmployee.save()
            messages.success(request, "Employee added successfully")
            return redirect("employees:index")
        else:
            messages.error(request, "Employee info is not valid")
            employeeForm = EmployeeForm(request.POST)
            context = {"employeeForm": employeeForm}
            return render(request, "employees/base_employees.html", context)
    return render(request, "employees/base_employees.html", context)


def create(request):

    # if request.method == "POST":
    #     form = EmployeeForm(request.POST)

    #     if form.is_valid():
    #         empInstance = form.save(commit=False)
    #         empInstance.save()
    #         messages.success(request, "Employee added successfully")
    #         return redirect("employees:index")
    #     else:
    #         print(form.errors)
    #         print(form.errors)
    #         messages.error(request, "Employee info is not valid")
    #         employeeForm = EmployeeForm(request.POST)
    #         context = {"employeeForm": employeeForm}

    #         return render(request, "employees/base_employees.html", context)

    return redirect("employees/")
