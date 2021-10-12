from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
    reverse,
)
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employee
from django.template.response import TemplateResponse

# Create your views here.


def index(request):
    employeeForm = EmployeeForm()
    employeeList = Employee.objects.order_by("last_name")
    context = {
        "employeeForm": employeeForm,
        "employeeList": employeeList,
    }

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            newEmployee = form.save(commit=False)
            newEmployee.save()
            messages.success(request, "Employee added successfully")
            return redirect("employees:index")
        else:
            messages.error(request, "Employee info not valid")
            employeeForm = EmployeeForm(request.POST)
            context = {"employeeForm": employeeForm}
            return render(request, "employees/base_employees.html", context)

    return render(request, "employees/base_employees.html", context)


def display(request, employeeID):
    displayEmployeeForm = EmployeeForm()
    employeeInfo = Employee.objects.get(emp_num=employeeID)
    displayEmployeeForm = EmployeeForm(instance=employeeInfo)
    response = TemplateResponse(
        request,
        "employees/display_employee.html",
        {"displayEmployeeForm": displayEmployeeForm},
    )
    response.render()
    print(response.content)
    return response
    # if request.method == "POST":
    #     displayEmployeeForm = EmployeeForm()
    #     employeeID = request.POST["employeeID"]
    #     employeeInfo = Employee.objects.get(emp_num=employeeID)
    #     displayEmployeeForm = EmployeeForm(instance=employeeInfo)

    #     return render(
    #         request,
    #         "employees/display_employee.html",
    #         {"displayEmployeeForm": displayEmployeeForm},
    #     )
