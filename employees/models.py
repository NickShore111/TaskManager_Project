from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.forms import widgets
from .validators import validate_employee_number

# Create your models here.


class Employee(models.Model):
    TITLES = (
        ("1", "Manager"),
        ("2", "Assistant Manager"),
        ("3", "Supervisor"),
        ("4", "Server"),
        ("5", "Busser"),
        ("6", "Bartender"),
        ("7", "Expo"),
        ("8", "Host"),
        ("9", "Barback"),
        ("20", "Chef"),
        ("21", "Sous Chef"),
        ("22", "Pantry"),
        ("23", "Line Cook"),
        ("24", "Grill Cook"),
        ("25", "Prep Cook"),
        ("26", "Fry Cook"),
        ("27", "Dishwasher"),
    )
    position = models.CharField(choices=TITLES, max_length=20)
    emp_num = models.CharField(
        max_length=4,
        unique=True,
        help_text="4 digit pin",
        validators=[validate_employee_number],
    )
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name, self.last_name


class Department(models.Model):
    employee = models.ForeignKey(Employee, on_delete=DO_NOTHING, default="99")
    LocationType = models.TextChoices("Location", "FoH BoH")
    location = models.CharField(blank=True, choices=LocationType.choices, max_length=20)
