'''ProfileSkillAdmin class'''

from django.contrib import admin

from common_files.admin.timestamp_active import TimestampActiveAdmin
from member_manager.models.profile_skill import ProfileSkill

@admin.register(ProfileSkill)
class ProfileSkillAdmin(TimestampActiveAdmin):
    '''ProfileSkillAdmin imports from TimestampActiveAdmin'''

    fields = ['profile', 'skill', 'created', 'created_by', 'modified',
              'modified_by']
    list_display = ['profile', 'skill']
    list_filter = ['skill']
    ordering = ['profile', 'skill']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['profile__last_name', 'profile__first_name',
                     'profile__email', 'skill__label']
