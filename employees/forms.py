from django.forms import ModelForm
from employees.models import Employee, Position, Department

# Create the form class.


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created_at']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
