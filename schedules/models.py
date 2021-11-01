from django.db import models
from employees.models import Positions
from django.utils import timezone
# Create your models here.

class Shifts(models.Model):
    DAYS = (
        ("SUN", "Sunday"),
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THUR", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
    )
    day_of_week = models.CharField(choices=DAYS, max_length=10)
    in_time = models.TimeField(default=timezone.now)
    out_time = models.TimeField(default=timezone.now)
    position = models.CharField(choices=Positions.TITLES, max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)