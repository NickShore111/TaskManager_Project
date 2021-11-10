from django.forms import ModelForm
from employees.models import Departments, Employees, Departments
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


# Create the form class. 


class EmployeeForm(ModelForm):
    # error_css_class = "error"
    class Meta:
        model = Employees
        fields = "__all__"

    def clean_login_num(self):
        login_num = self.cleaned_data.get("login_num")
        if len(login_num) < 4:
            raise ValidationError(_("Invalid ID Number."))
        else:
            try:
                login_num = int(login_num)
            except ValueError:
                raise ValidationError(_("Invalid ID Number."))
        return login_num


class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"
