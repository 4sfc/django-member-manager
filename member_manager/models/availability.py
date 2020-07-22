'''Availability class'''

from django.db import models

from common_files.models.timestamp_weekday_hour import TimestampWeekdayHour
from member_manager.models.profile import Profile

class Availability(TimestampWeekdayHour):
    '''Availability has profile, weekday, start and end times'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} - {}'.format(self.get_weekday_display(),
                                   self.get_start_time_display(),
                                   self.get_end_time_display())

    class Meta:
        app_label = 'member_manager'
        constraints = [
            models.UniqueConstraint(
                fields=['profile', 'weekday', 'start_time'],
                name='unique_availability')
        ]
        indexes = [
            models.Index(fields=['weekday', 'start_time'],
                         name='weekday_start_index'),
            models.Index(fields=['start_time', 'end_time'],
                         name='start_end_index'),
        ]
        ordering = ['profile', 'weekday', 'start_time']
        verbose_name_plural = 'availability'
