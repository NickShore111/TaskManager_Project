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
    empPk = employeePK
    employee = Employee.objects.get(pk=empPk)
    # print("employee: ", employee)
    editEmployeeForm = EmployeeForm(instance=employee)
    context = {"editEmployeeForm": editEmployeeForm,
                "employee": employee}
    return render(request, "employees/base_editEmployees.html", context)
    
def update(request, employeePK):
    empPk = employeePK
    employeeForm = EmployeeForm(request.POST)
    if employeeForm.is_valid():
        employee = Employee.objects.get(pk=empPk)
        editEmployee = EmployeeForm(request.POST, instance=employee)
        editEmployee.save()
        messages.success(request, "Employee Data Updated Successfully")
        return redirect("employees:index")
    else:
        messages.error(request, "Updating Employee Data Not Valid")
        context = {"editEmployeeForm": employeeForm,
                    "employee": empPk}
        print(empPk)
        return render(request, "employees/base_editEmployees.html", context)

def delete(request, employeePK):
    empPk = employeePK
    Employee.objects.get(pk= empPk).delete()
    return redirect("employees:index")

def create(request):
    if request.method == "GET":
        employeeForm = EmployeeForm()
        context = {"employeeForm": employeeForm}
        return render(request, "employees/base_createEmployee.html", context)
    elif request.method == "POST":
        employeeForm = EmployeeForm(request.POST)
        if employeeForm.is_valid():
            employeeForm.save()
            messages.success(request, "New Employee Successfully Created")
            return redirect("employees:create")
        else:
            employeeForm = EmployeeForm(request.POST)
            messages.error(request, "Employee Data Not Valid")
            context = {"employeeForm": employeeForm}
            return render(request, "employees/base_createEmployee.html", context)
