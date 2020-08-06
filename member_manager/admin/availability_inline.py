"""AvailabilityInline class"""

from django.contrib import admin

from member_manager.forms.availability_inline_formset import (
    AvailabilityInlineFormSet
)
from member_manager.models.availability import Availability


class AvailabilityInline(admin.TabularInline):
    """AvailabilityInline inherits from TabularInline"""

    model = Availability
    formset = AvailabilityInlineFormSet
    extra = 1
    fk_name = 'profile'
    ordering = ['weekday', 'start_time', 'end_time']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['profile__last_name', 'profile__first_name',
                     'profile__email']
