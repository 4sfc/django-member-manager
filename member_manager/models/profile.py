"""Profile class"""

from django.contrib.auth.models import User
from django.db import models

from common_files.models.timestamp import Timestamp


class Profile(Timestamp):
    """Profile has first, last, email, pronouns, and phone fields"""

    first_name = models.CharField(db_index=True, max_length=191)
    last_name = models.CharField(db_index=True, max_length=191)
    pronouns = models.CharField(max_length=191, blank=True, null=True)
    email = models.EmailField(db_index=True, max_length=191, unique=True)
    phone = models.PositiveIntegerField(help_text='Enter only numbers.',
                                        blank=True, null=True)
    active = models.BooleanField(default=True, null=False)
    user = models.OneToOneField(User, blank=True, null=True,
                                on_delete=models.CASCADE)
    joined = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        app_label = 'member_manager'
        constraints = [
            models.UniqueConstraint(fields=['user', 'last_name', 'email'],
                                    name='unique_profile')
        ]
        indexes = [
            models.Index(fields=['last_name', 'email'],
                         name='last_name_email_index'),
            models.Index(fields=['last_name', 'first_name'],
                         name='last_first_name_index'),
            models.Index(fields=['last_name'], name='last_name_index'),
            models.Index(fields=['email'], name='email_index'),
            models.Index(fields=['active'], name='active_index'),
            models.Index(fields=['user'], name='user_index'),
        ]
        ordering = ['last_name', 'first_name', 'email']
        verbose_name_plural = 'profiles'
