'''ProfileAdmin class'''

from django.contrib import admin

from common_files.admin.timestamp import TimestampAdmin
from member_manager.admin.availability_inline import AvailabilityInline
from member_manager.admin.profile_skill_inline import ProfileSkillInline
from member_manager.models.profile import Profile

@admin.register(Profile)
class ProfileAdmin(TimestampAdmin):
    '''ProfileAdmin shows profile, availability, and skill data'''

    fields = ['last_name', 'first_name', 'user', 'active', 'pronouns',
              'email', 'phone', 'joined', 'notes', 'created', 'created_by',
              'modified', 'modified_by']
    inlines = [AvailabilityInline, ProfileSkillInline]
    list_display = ['last_name', 'first_name', 'user', 'active', 'email',
                    'phone']
    list_display_links = ['last_name', 'first_name', 'user']
    list_filter = ['active', 'user__is_superuser', 'user__is_staff']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    show_full_result_count = True
    search_fields = ['last_name', 'first_name', 'user__username', 'email',
                     'phone']
    sortable_by = ['last_name', 'first_name', 'user', 'active',
                   'email', 'phone', 'joined']
