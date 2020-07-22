'''ProfileSkill class'''

from django.db import models

from common_files.models.timestamp import Timestamp
from member_manager.models.profile import Profile
from member_manager.models.skill import Skill

class ProfileSkill(Timestamp):
    '''ProfileSkill has profile and skill fields'''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.profile, self.skill)

    class Meta:
        app_label = 'member_manager'
        constraints = [
            models.UniqueConstraint(fields=['profile', 'skill'],
                                    name='unique_profile_skill')
        ]
        indexes = [
            models.Index(fields=['profile'], name='profile_index')
        ]
        ordering = ['profile', 'skill']
        verbose_name_plural = 'profile skills'
