from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from employees.models import Employees
from datetime import date
from django.utils import timezone


# Create your models here.

class EventsHasEmployees(models.Model):
    event = models.OneToOneField("Events", on_delete=models.DO_NOTHING, primary_key=True)
    employee = models.ForeignKey(Employees, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'events_has_employees'
        unique_together = (('event', 'employee'),)

class Events(models.Model):
    title = models.CharField(max_length=45)
    notes = models.TextField(max_length=200, blank=True, null=True)
    day = models.DateField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    assigned_by = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, related_name='Event_assigned_by')
    assigned_to = models.ManyToManyField(Employees, through="EventsHasEmployees")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'events'

    def get_absolute_url(self):
        return reverse('events:detail', kwargs={'pk': self.pk})



# class Event(models.Model):
#     title = models.CharField('Title', max_length=30)
#     day = models.DateField('Day of the event', help_text='Day of the event')
#     start_time = models.TimeField('Starting time', help_text='Starting time')
#     end_time = models.TimeField('Final time', help_text='Final time')
#     notes = models.TextField(
#         'Event Notes', help_text='Event Notes', blank=True, null=True)

#     class Meta:
#         verbose_name = 'Event'
#         verbose_name_plural = 'Event'

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
        url = reverse('admin:%s_%s_change' % (
            self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.title))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must end after starting times')

        events = Events.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.title) + ':' + str(event.start_time) + '-' + str(event.end_time))
