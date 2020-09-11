"""Page class"""

from django.db import models

from common_files.models.timestamp import Timestamp


class Page(Timestamp):
    """Page has title, slug, content, public, and published fields"""

    title = models.CharField(max_length=191)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    content = models.TextField()
    public = models.BooleanField(default=False)
    published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'member_manager'
        ordering = ['title', 'slug']
        verbose_name_plural = 'pages'
