from django.db import models
from employees.models import Employees, Positions

# Create your models here.
class Reminders(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.CharField(max_length=45, blank=True, null=True)
    updated_at = models.CharField(max_length=45, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)

    class Meta:
        db_table = 'reminders'


class Tasks(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'tasks'


class TasksHasPositions(models.Model):
    task = models.OneToOneField(Tasks, models.DO_NOTHING, primary_key=True)
    position = models.ForeignKey(Positions, models.DO_NOTHING)

    class Meta:
        db_table = 'tasks_has_positions'
        unique_together = (('task', 'position'),)
