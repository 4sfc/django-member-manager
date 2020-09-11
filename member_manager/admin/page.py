"""PageAdmin class"""

from django.contrib import admin

from common_files.admin.timestamp import TimestampAdmin
from member_manager.models.page import Page


@admin.register(Page)
class PageAdmin(TimestampAdmin):
    """PageAdmin inherits from TimestampAdmin"""

    fields = ['title', 'slug', 'content', 'public', 'published']
    list_display = ['title', 'slug', 'content', 'public', 'published']
    list_filter = ['public']
    ordering = ['title', 'slug', 'public']
    readonly_fields = ['created', 'created_by', 'modified', 'modified_by']
    search_fields = ['title', 'slug', 'content']
