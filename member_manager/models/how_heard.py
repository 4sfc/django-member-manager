"""HowHeard class"""

from common_files.models.base import Base


class HowHeard(Base):
    """HowHeard has label, value, and active fields"""

    class Meta:
        app_label = 'member_manager'
        ordering = ['label', 'active']
        verbose_name_plural = 'how heard'
