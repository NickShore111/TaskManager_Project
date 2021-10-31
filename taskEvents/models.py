from django.db import models
from employees.models import Employees, Positions
from django.utils.translation import gettext_lazy as _

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

    class TaskFrequency(models.TextChoices):
        SHIFT_START = 'SH_ST', _('Beginning of Shift')
        SHIFT_MID = 'SH_MD', _('Middle of Shift')
        SHIFT_END = 'SH_EN', _('End of Shift')
        DAY_START = 'D_ST', _('Start of Day')
        DAY_MID = 'D_MD', _('Middle of Day')
        DAY_END = 'D_EN', _('End of Day')
        WEEK_START = 'WK_ST', _('Start of Week')
        WEEK_MID = 'WK_MD', _('Middle of Week')
        WEEK_END = 'WK_EN', _('End of Week')
        SHIFT = 'SH', _('Once Per Shift')
        DAILY = 'DLY', _('Once Per Day')
        WEEKLY = 'WKLY', _('Once Per Week')
        MONTHLY = 'MNTH', _('Once Per Month')
        YEARLY = 'YRLY', _('Once Per Year')
        QUARTERLY = 'QTLY', _('Once Per Yearly Quarter')

    position = models.ForeignKey(Positions, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField('Task', max_length=45)
    description = models.CharField(max_length=200, blank=True, null=True)
    frequency = models.CharField(max_length=5, choices=TaskFrequency.choices, default=TaskFrequency.SHIFT)
    time_allocation = models.PositiveIntegerField(help_text="Appx. Minutes")
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'tasks'

