from django.forms import ModelForm
from employees.models import Departments, Employees, Departments
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Create the form class. 


class EmployeeForm(ModelForm):
    error_css_class = "error"
    class Meta:
        model = Employees
        fields = "__all__"
        exclude = ["created_at"]

    def clean_emp_num(self):
        emp_num = self.cleaned_data.get("emp_num")
        if len(emp_num) < 4:
            raise ValidationError(_("Invalid ID Number."))
        else:
            try:
                emp_num = int(emp_num)
            except ValueError:
                raise ValidationError(_("Invalid ID Number."))
        return emp_num


class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"
