from django.forms import ModelForm
from schedules.models import Schedule, Shifts

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

class ShiftForm(ModelForm):
    class Meta:
        model = Shifts
        fields = '__all__'