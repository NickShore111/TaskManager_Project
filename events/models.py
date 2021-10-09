from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.


class Event(models.Model):
    title = models.CharField('Title', max_length=30)
    day = models.DateField('Day of the event', help_text='Day of the event')
    start_time = models.TimeField('Starting time', help_text='Starting time')
    end_time = models.TimeField('Final time', help_text='Final time')
    notes = models.TextField(
        'Event Notes', help_text='Event Notes', blank=True, null=True)

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
        url = reverse('admin:%s_%s_change' % (
            self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.title))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must end after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.title) + ':' + str(event.start_time) + '-' + str(event.end_time))
