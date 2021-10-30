from django.db import models
from employees.models import Employees, Positions

# Create your models here.
# class Reminders(models.Model):
#     name = models.CharField(max_length=45)
#     deadline = models.DateTimeField(blank=True, null=True)
#     created_at = models.CharField(max_length=45, blank=True, null=True)
#     updated_at = models.CharField(max_length=45, blank=True, null=True)
#     reminder_for = models.ForeignKey(Employees, models.DO_NOTHING)

#     class Meta:
#         db_table = 'reminders'


class Tasks(models.Model):
    position = models.ForeignKey(Positions, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200, blank=True, null=True)
    time_allocation = models.PositiveIntegerField(help_text="Hours to complete")
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'tasks'

