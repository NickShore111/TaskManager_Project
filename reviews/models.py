from django.db import models
from employees.models import Employees
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse
from employees.models import Employees
from datetime import date
# Create your models here.


class Reviews(models.Model):

    class Rating(models.IntegerChoices):
        NOT_APPLICABLE = 0
        UNACCEPTABLE = 1
        NEEDS_IMPROVEMENT = 2
        SATISFACTORY = 3
        ABOVE_AVERAGE = 4
        EXCEPTIONAL = 5
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    attendance = models.IntegerField(choices=Rating.choices)
    grooming = models.IntegerField(choices=Rating.choices)
    punctuality = models.IntegerField(choices=Rating.choices)
    attire = models.IntegerField(choices=Rating.choices)
    teamwork = models.IntegerField(choices=Rating.choices)
    initiative = models.IntegerField(choices=Rating.choices)
    service = models.IntegerField(choices=Rating.choices)
    quality = models.IntegerField(choices=Rating.choices)
    productivity = models.IntegerField(choices=Rating.choices)
    created_at = models.DateField(verbose_name='Date', default=date.today)

    class Meta:
        db_table = 'reviews'

    def get_absolute_url(self):
        return reverse('reviews:detail', kwargs={'pk': self.pk})

# class Review(models.Model):

#     class Rating(models.IntegerChoices):
#         UNACCEPTABLE = 1
#         NEEDS_IMPROVEMENT = 2
#         SATISFACTORY = 3
#         ABOVE_AVERAGE = 4
#         EXCEPTIONAL = 5

#     employee = models.ForeignKey(Employee, on_delete=DO_NOTHING)
#     attendance = models.IntegerField(choices=Rating.choices)
#     grooming = models.IntegerField(choices=Rating.choices)
#     punctuality = models.IntegerField(choices=Rating.choices)
#     attire = models.IntegerField(choices=Rating.choices)
#     teamwork = models.IntegerField(choices=Rating.choices)
#     initiative = models.IntegerField(choices=Rating.choices)
#     customer_service = models.IntegerField(choices=Rating.choices)
#     performance = models.IntegerField(choices=Rating.choices)
#     created_at = models.DateField(auto_now_add=True)

#     def get_absolute_url(self):
#         return reverse('reviews:detail', kwargs={'pk': self.pk})


