from django.contrib import admin
from employees.models import *

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)
