from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from employees.models import Employees
from datetime import date
from django.utils import timezone


# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=30)
    notes = models.TextField(
        'Details', blank=True, null=True)
    day = models.DateField('Day of Event')
    start_time = models.TimeField('Begins', default=timezone.now)
    end_time = models.TimeField('Ends', default=timezone.now)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Event'

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:  # edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):  # innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
            overlap = True

        return overlap


    def get_absolute_url(self):
        url = ('update/%s' % (
            self.id))
        return u'<a href="%s">%s</a>' % (url, str(self.title))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must end after starting times')

        events = Events.objects.filter(day=self.day)
        """Could not prevent validation from preventing update"""
        # if events.exists():
            # for event in events:
            #     if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
            #         raise ValidationError(
            #             'There is an overlap with another event: ' + str(event.day) + ', ' + str(
            #                 event.title) + ':' + str(event.start_time) + '-' + str(event.end_time))
