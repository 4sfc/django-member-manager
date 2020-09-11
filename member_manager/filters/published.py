"""PublishedFilter class"""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PublishedListFilter(admin.SimpleListFilter):
    """PublishedListFilter filters published and unpublished pages"""

    title = _('published')
    parameter_name = 'published'

    def lookups(self, request, model_admin):
        return (
            ('published', _('Yes')),
            ('unpublished', _('No')),
        )

    def queryset(self, request, queryset):
        """Return queryset of published or unpublished pages."""
        if not self.value():
            return queryset

        if self.value() == 'published':
            updated_qs = queryset.filter(published__isnull=False)
        elif self.value() == 'unpublished':
            updated_qs = queryset.filter(published__isnull=True)
        return updated_qs
