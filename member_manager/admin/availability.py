'''AvailabilityAdmin class'''

from django.contrib import admin

from common_files.admin.timestamp import TimestampAdmin
from common_files.filters.start_time import StartTimeListFilter
from member_manager.forms.availability import AvailabilityForm
from member_manager.models.availability import Availability

@admin.register(Availability)
class AvailabilityAdmin(TimestampAdmin):
    '''AvailabilityAdmin inherits from TimestampAdmin'''

    fields = ['profile', 'weekday', 'start_time', 'end_time',
              'created', 'created_by', 'modified', 'modified_by']
    form = AvailabilityForm
    list_display = ['profile', 'weekday', 'start_time', 'end_time']
    list_filter = ['profile__active', 'weekday', StartTimeListFilter]
    ordering = ['profile__last_name', 'profile__first_name', 'weekday',
                'start_time']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['profile__last_name', 'profile__first_name',
                     'profile__email']
