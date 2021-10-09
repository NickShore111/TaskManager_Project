from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class Employee(models.Model):
    emp_num = models.IntegerField(
        name="Employee #", unique=True, help_text="4 number pin")
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    start_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    position = models.ForeignKey('Position', on_delete=DO_NOTHING)

    def __str__(self):
        return self.first_name, self.last_name


class Position(models.Model):
    TITLES = (
        ('1', 'Manager'),
        ('2', 'Assistant Manager'),
        ('3', 'Supervisor'),
        ('4', 'Server'),
        ('5', 'Busser'),
        ('6', 'Bartender'),
        ('7', 'Expo'),
        ('8', 'Host'),
        ('9', 'Barback'),
        ('20', 'Chef'),
        ('21', 'Sous Chef'),
        ('22', 'Pantry'),
        ('23', 'Line Cook'),
        ('24', 'Grill Cook'),
        ('25', 'Prep Cook'),
        ('26', 'Fry Cook'),
        ('27', 'Dishwasher'),
    )
    title = models.IntegerField(choices=TITLES)
    location = models.ForeignKey('Department', on_delete=DO_NOTHING)


class Department(models.Model):
    department = models.TextChoices('Locations', 'FoH BoH')
