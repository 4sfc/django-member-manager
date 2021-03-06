"""SkillAdmin class"""

from django.contrib import admin

from common_files.admin.base import BaseAdmin
from member_manager.models.skill import Skill


@admin.register(Skill)
class SkillAdmin(BaseAdmin):
    """SkillAdmin inherits from BaseAdmin"""

    fields = ['label', 'value', 'active', 'created', 'created_by',
              'modified', 'modified_by']
    list_display = ['label', 'value', 'active']
    list_filter = ['active']
    ordering = ['-active', 'label']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['label', 'value']
