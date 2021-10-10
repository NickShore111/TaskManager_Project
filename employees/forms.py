from django.forms import ModelForm, IntegerField
from employees.models import Employee, Position, Department
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create the form class.


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ["created_at", "position"]

    def clean_emp_num(self):
        emp_num = self.cleaned_data.get("emp_num")
        if len(emp_num) < 4:
            raise ValidationError(_("Invalid Employee ID Number."))
        else:
            try:
                emp_num = int(self)
            except ValueError:
                raise ValidationError(_("Employee ID must be 4 digits."))
        return emp_num


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ["title"]


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
