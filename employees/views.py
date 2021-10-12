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
    employeeList = Employee.objects.all()
    context = {
        "employeeList": employeeList,
    }
    # employeeForm = EmployeeForm()

    # """Saving new employee data"""
    # if request.method == "POST":
    #     newEmployee = EmployeeForm(request.POST)
    #     if newEmployee.is_valid():
    #         newEmployee.save()
    #         messages.success(request, "Employee added successfully")
    #         return redirect("employees:index")
    #     else:
    #         messages.error(request, "Employee info not valid")
    #         employeeForm = EmployeeForm(request.POST)
    #         context = {"employeeForm": employeeForm}
    #         return render(request, "employees/base_employees.html", context)

    return render(request, "employees/base_employees.html", context)


def edit(request, employeePK=""):
    employeeInfo = Employee.objects.get(pk=employeePK)
    editEmployeeForm = EmployeeForm(instance=employeeInfo)
    if request.method == "GET":
        return render(
            request,
            "employees/base_editEmployees.html",
            {"editEmployeeForm": editEmployeeForm},
        )
    elif request.method == "POST":
        updateEmployeeForm = EmployeeForm(request.POST)
        if updateEmployeeForm.is_valid():
            updateEmployeeForm.save()
            messages.success(request, "Employee Data Updated Successfully")
            return redirect("edit/" + employeePK)
        else:
            messages.error(request, "Updated Employee Data Returned Invalid")
            context = {"updateEmployeeForm": updateEmployeeForm}
            context = {
                "editEmployeeForm": updateEmployeeForm,
            }
            return render(request, "employees/base_editEmployees.html", context)


# def create(request):

#     if request.method == "GET":
#         employeeForm = EmployeeForm()

#         return render(
#             request, "employees/base_editEmployees.html", {"employeeForm": employeeForm}
#         )


# def edit(request, employeePK=""):
#     if request.method == "GET":
#         displayEmployeeForm = EmployeeForm()
#         employeeInfo = Employee.objects.get(pk=employeePK)
#         displayEmployeeForm = EmployeeForm(instance=employeeInfo)
#         return TemplateResponse(
#             request,
#             "employees/base_editEmployees.html",
#             {"displayEmployeeForm": displayEmployeeForm},
#         )
#     elif request.method == "POST":
#         updateEmployeeForm = EmployeeForm(request.POST)
#         if updateEmployeeForm.is_valid():
#             updateEmployeeForm.save()
#             messages.success(request, "Employee updated successfully")
#             return redirect("employees:index")
#         else:
#             messages.error(request, "Empoyee update info not valid")
#             context = {"updateEmployeeForm": updateEmployeeForm}
#             employeeForm = EmployeeForm()
#             employeeList = Employee.objects.order_by("last_name")
#             context = {
#                 "employeeForm": employeeForm,
#                 "employeeList": employeeList,
#                 "updateEmployeeForm": updateEmployeeForm,
#             }
#             return TemplateResponse(
#                 request, "employees/base_editEmployees.html", context
#             )
