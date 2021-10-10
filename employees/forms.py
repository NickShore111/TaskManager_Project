from django.forms import ModelForm, IntegerField
from employees.models import Employee, Position, Department
from django.utils.translation import gettext_lazy as _
# Create the form class.


class EmployeeForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created_at', 'position']
        # error_messages = {
        #     'emp_id': {
        #         'not_unique': _("Employee ID is already in use.")
        #     }
        # }


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['title']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
