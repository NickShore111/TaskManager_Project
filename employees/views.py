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
    model = Employees
class EmployeeFormView(FormView):
    form_class = EmployeeForm
    template_name = "employees/employees_form.html"
class EmployeeCreateView(CreateView):
    model = Employees
    fields = '__all__'
    success_url = "/taskmanager/employees/list/"
class EmployeeUpdateView(UpdateView):
    model = Employees
    fields = '__all__'
    success_url = "/taskmanager/employees/list/"
class EmployeeDeleteView(DeleteView):
    model = Employees
    fields = '__all__'
    success_url = reverse_lazy('employee-form')

def index(request):
    employeeList = Employees.objects.all()
    context = {
        "employeeList": employeeList,
    }
    return render(request, "employees/base_employees.html", context)

# def update(request, employeePK=0):
#     employee = Employees.objects.get(pk=employeePK)
#     form = EmployeeForm(instance=employee)
#     context = {"editEmployeeForm": form,
#                 "employee": employee}
#     if request.method == "GET":
#         return render(request, "employees/base_editEmployees.html", context)
#     elif request.method == "POST":
#         newForm = EmployeeForm(request.POST)
#         initialData = { 
#             'login_num': employee.login_num, 
#             'username': employee.username, 
#             'first_name': employee.first_name, 
#             'last_name': employee.last_name, 
#             'email': employee.email, 
#             'phone': employee.phone, 
#             'start_date': employee.start_date, 
#             'position': employee.position, 
#         }
#         checkForChange = EmployeeForm(request.POST, initial=initialData)
#         if newForm.is_valid() and checkForChange.has_changed():
#             editEmployee = EmployeeForm(request.POST, instance=employee)
#             editEmployee.save()
#             messages.success(request, "Employee Data Updated Successfully")
#             return redirect("employees:index")
#         elif not checkForChange.has_changed():
#             messages.error(request, "No Employee Data Changed")
#             return render(request, 'employees/base_editEmployees.html', context)
#         else:
#             messages.error(request, "New Employee Data Not Valid")
#             return render(request, 'employees/base_editEmployees.html', context)

# def delete(request, employeePK):
#     Employees.objects.get(pk= employeePK).delete()
#     return redirect("employees:index")

# def create(request):
#     if request.method == "GET":
#         employeeForm = EmployeeForm()
#         context = {"employeeForm": employeeForm}
#         return render(request, "employees/base_createEmployee.html", context)
#     elif request.method == "POST":
#         employeeForm = EmployeeForm(request.POST)
#         context = {"employeeForm": employeeForm}
#         if employeeForm.is_valid():
#             employeeForm.save()
#             messages.success(request, "New Employee Successfully Created")
#             return redirect("employees:create")
#         else:
#             messages.error(request, "Employee Data Not Valid")
#             return render(request, "employees/base_createEmployee.html", context)
