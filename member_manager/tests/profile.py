"""ProfileTest class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Profile


class ProfileTest(TestCase):
    """Test Profile model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo', email='foo@example.com')

    def test_str(self):
        """Test Profile string"""
        a_profile = Profile.objects.create(first_name='foo',
                                           last_name='bar',
                                           email='foo@example.com',
                                           user=self.user,
                                           created_by=self.user,
                                           modified_by=self.user)
        self.assertEqual(str(a_profile), 'foo bar')
