from django.db import models
from employees.models import Positions
from datetime import date# Create your models here.

class Shifts(models.Model):
    date = models.ForeignKey("Schedule", models.DO_NOTHING)
    HOURS = (
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
        ("19", "19"),
        ("20", "20"),
        ("21", "21"),
        ("22", "22"),
    )
    in_time_hr = models.TimeField("In", choices=HOURS)
    out_time_hr = models.TimeField("Out", choices=HOURS)
    position = models.CharField(choices=Positions.TITLES, max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)


class Schedule(models.Model):
    date = models.DateField(default=date.today, unique=True)
