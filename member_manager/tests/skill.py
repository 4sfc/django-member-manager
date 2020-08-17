"""SkillTest class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Skill


class SkillTest(TestCase):
    """Test Skill model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo', email='foo@example.com')
        cls.skill = Skill.objects.create(label='Programming', value='pr',
                                         created_by=cls.user,
                                         modified_by=cls.user)

    def test_str(self):
        """Test Skill string"""
        self.assertEqual(str(self.skill), 'Programming')
