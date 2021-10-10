from django.http.response import HttpResponseRedirect
from django.shortcuts import (
    render,
    redirect,
    HttpResponse,
    HttpResponseRedirect,
    reverse,
)
from django.contrib import messages
from .forms import EmployeeForm, PositionForm
from .models import Employee

# Create your views here.


def index(request):
    employeeForm = EmployeeForm()
    positionForm = PositionForm()

    context = {"employeeForm": employeeForm, "positionForm": positionForm}
    return render(request, "employees/base_employees.html", context)


def create(request):

    if request.method == "POST":
        newEmployee = EmployeeForm(request.POST)
        # print(request.POST)
        if newEmployee.is_valid():

            # title = request.POST["title"]
            # emp_num = newEmployee.cleaned_data["emp_num"]
            # firstname = newEmployee.cleaned_data["first_name"]
            # lastname = newEmployee.cleaned_data["last_name"]
            # username = newEmployee.cleaned_data["username"]
            # email = newEmployee.cleaned_data["email"]
            # phone_number = newEmployee.cleaned_data["phone_number"]
            # start_date = newEmployee.cleaned_data["start_date"]

            # emp = Employee(
            #     first_name=firstname,
            #     last_name=lastname,
            #     emp_num=emp_num,
            #     username=username,
            #     email=email,
            #     phone_number=phone_number,
            #     start_date=start_date,
            #     position_id=title,
            # )
            # emp.save()
            print("successfully added")
            messages.success(request, "Employee added successfully")
            return HttpResponseRedirect(reverse("dashboard:index"))
        else:
            print(newEmployee.errors)
            messages.error(request, "Employee info is not valid")
            employeeForm = EmployeeForm(request.POST)
            positionForm = PositionForm()
            context = {"employeeForm": employeeForm, "positionForm": positionForm}

            return render(request, "employees/base_employees.html", context)

    return redirect("employees/")
