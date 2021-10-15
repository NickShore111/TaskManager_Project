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

# Create your views here.


def index(request):
    employeeList = Employee.objects.all()
    context = {
        "employeeList": employeeList,
    }
    return render(request, "employees/base_employees.html", context)


def edit(request, employeePK=0):
    if request.method == "GET":
        employee = Employee.objects.get(pk=employeePK)
        editEmployeeForm = EmployeeForm(instance=employee)
        return render(request, "employees/base_editEmployees.html", {"editEmployeeForm": editEmployeeForm})
    elif request.method == "POST":
        employeeForm = EmployeeForm(request.POST)
        if employeeForm.is_valid():
            employee = Employee.objects.get(pk=employeePK)
            editEmployee = EmployeeForm(request.POST, instance=employee)
            editEmployee.save()
            messages.success(request, "Employee Data Updated Successfully")
            context = {"editEmployeeForm": employeeForm}

            return redirect("edit/"+employeePK, context)
        else:
            messages.error(request, "Updated Employee Data Returned Invalid")
            context = {"editEmployeeForm": employeeForm}
            return redirect("edit/"+employeePK, context)


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
