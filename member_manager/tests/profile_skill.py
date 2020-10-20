"""ProfileSkillTest class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Profile
from member_manager.models import ProfileSkill
from member_manager.models import Skill


class ProfileSkillTest(TestCase):
    """Test ProfileSkill model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo', email='foo@example.com')
        cls.profile = Profile.objects.create(first_name='foo', last_name='bar',
                                             email='foo@example.com',
                                             phone='1234567890',
                                             user=cls.user,
                                             created_by=cls.user,
                                             modified_by=cls.user)
        cls.skill = Skill.objects.create(label='Programming', value='pr',
                                         created_by=cls.user,
                                         modified_by=cls.user)

    def test_str(self):
        """Test ProfileSkill string"""
        a_profile = ProfileSkill.objects.create(profile=self.profile,
                                                skill=self.skill,
                                                created_by=self.user,
                                                modified_by=self.user)
        self.assertEqual(str(a_profile), 'foo bar - Programming')
