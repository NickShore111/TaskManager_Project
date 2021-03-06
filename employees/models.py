from django.db import models
from .validators import validate_employee_number

# Create your models here.

class Departments(models.Model):
    LocationType = models.TextChoices('LocationType', 'FoH BoH')
    location = models.CharField(blank=True, choices=LocationType.choices, max_length=20, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'departments'

class Positions(models.Model):
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
    title = models.CharField(choices=TITLES, max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'positions'

class Employees(models.Model):
    position = models.ForeignKey('Positions', models.DO_NOTHING)
    login_num = models.CharField(        
        verbose_name="Employee #",
        max_length=4,
        # unique=True,
        help_text="4 digit pin",
        validators=[validate_employee_number],
)
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    phone = models.CharField(max_length=45)
    start_date = models.DateField()
    status = models.BooleanField(help_text='Check if active', default=True, blank=False, null=False)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'employees'
