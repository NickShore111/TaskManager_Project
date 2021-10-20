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
    print(employeePK)
    empPk = employeePK
    print(empPk)
    if request.method == "GET":
        employee = Employee.objects.get(pk=empPk)
        print("employee: ", employee)
        editEmployeeForm = EmployeeForm(instance=employee)
        context = {"editEmployeeForm": editEmployeeForm,
                    "employee": employee}
        return render(request, "employees/base_editEmployees.html", context)
    elif request.method == "POST":
        empPk = employeePK
        employeeForm = EmployeeForm(request.POST)
        if employeeForm.is_valid():

            employee = Employee.objects.get(pk=empPk)
            editEmployee = EmployeeForm(request.POST, instance=employee)
            editEmployee.save()
            messages.success(request, "Employee Data Updated Successfully")
            # context = {"editEmployeeForm": employeeForm,
            #             "employee": employee}

            return redirect("emloyees:index")
        else:
            messages.error(request, "Updated Employee Data Returned Invalid")
            context = {"editEmployeeForm": employeeForm,
                        "employee": empPk}
            return redirect("edit/"+employeePK, context)

def update(request, employeePK):
    empPk = employeePK
    employeeForm = EmployeeForm(request.POST)
    if employeeForm.is_valid():

        employee = Employee.objects.get(pk=empPk)
        editEmployee = EmployeeForm(request.POST, instance=employee)
        editEmployee.save()
        messages.success(request, "Employee Data Updated Successfully")
        # context = {"editEmployeeForm": employeeForm,
        #             "employee": employee}

        return redirect("emloyees:index")
    else:
        messages.error(request, "Updated Employee Data Returned Invalid")
        context = {"editEmployeeForm": employeeForm,
                    "employee": empPk}
        return redirect("edit/"+employeePK, context)
    pass

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
