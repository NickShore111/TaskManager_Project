from django.db import models
from employees.models import Employee
from django.db.models.deletion import DO_NOTHING
from django.core.validators import MaxValueValidator

# Create your models here.
class Review(models.Model):

    class Rating(models.IntegerChoices):
        UNACCEPTABLE = 1
        NEEDS_IMPROVEMENT = 2
        SATISFACTORY = 3
        ABOVE_AVERAGE = 4
        EXCEPTIONAL = 5

    employee = models.ForeignKey(Employee, on_delete=DO_NOTHING)
    attendance = models.IntegerField(choices=Rating.choices)
    grooming = models.IntegerField(choices=Rating.choices)
    punctuality = models.IntegerField(choices=Rating.choices)
    attire = models.IntegerField(choices=Rating.choices)
    teamwork = models.IntegerField(choices=Rating.choices)
    initiative = models.IntegerField(choices=Rating.choices)
    customer_service = models.IntegerField(choices=Rating.choices)
    performance = models.IntegerField(choices=Rating.choices)
    created_at = models.DateField(auto_now_add=True)

