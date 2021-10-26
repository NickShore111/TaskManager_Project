from django.contrib import admin
from employees.models import *

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employees, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Departments, DepartmentAdmin)
