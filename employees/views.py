from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import EmployeeForm, PositionForm
from .models import Employee

# Create your views here.


def index(request):
    if request.method == 'POST':
        newEmployee = EmployeeForm(request.POST)
        empPosition = PositionForm(request.POST)
        if newEmployee.is_valid() and empPosition.is_valid():
            # process data, add to db
            print("request.post:")
            print(request.POST)
            title = empPosition.cleaned_data['title']
            emp_num = newEmployee.cleaned_data['Employee #']
            firstname = newEmployee.cleaned_data['first_name']
            lastname = newEmployee.cleaned_data['last_name']
            username = newEmployee.cleaned_data['username']
            email = newEmployee.cleaned_data['email']
            phone_number = newEmployee.cleaned_data['phone_number']
            start_date = newEmployee.cleaned_data['start_date']

            emp = Employee(first_name=firstname, last_name=lastname, emp_num=emp_num,
                           username=username, email=email, phone_number=phone_number, start_date=start_date, position_id=title)
            # emp.save()
            messages.success(request, 'Employee added successfully')
            return HttpResponseRedirect('/taskmanager/employees/')
        else:
            newEmployee = EmployeeForm(request.POST)
            messages.error(request, 'Emloyee info is not valid')

            return render(request, "employees/base_employees.html", {'employeForm': newEmployee})

    elif request.method == 'GET':

        employeeForm = EmployeeForm()
        positionForm = PositionForm()
        context = {
            "employeeForm": employeeForm,
            "positionForm": positionForm}
    return render(request, "employees/base_employees.html", context)


def create(request):
    print("Employee for is Valid")
    print("Entered created def")
    return redirect('employees/')
