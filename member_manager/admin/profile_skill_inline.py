'''ProfileSkill class'''

from common_files.admin.active_tabular_inline import ActiveTabularInline
from member_manager.models.profile_skill import ProfileSkill

class ProfileSkillInline(ActiveTabularInline):
    '''ProfileSkillInline inherits from ActiveTabularInline'''

    model = ProfileSkill
    extra = 1
    fk_name = 'profile'
    ordering = ['skill']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['profile__last_name', 'profile__first_name',
                     'profile__email', 'skill__label']
