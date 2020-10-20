"""AvailabilityTest class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Availability
from member_manager.models import Profile


class AvailabilityTest(TestCase):
    """Test Availability model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo',
                                       email='foo@example.com')
        cls.profile = Profile.objects.create(first_name='foo',
                                             last_name='bar',
                                             email='foo@example.com',
                                             phone='1234567890',
                                             user=cls.user,
                                             created_by=cls.user,
                                             modified_by=cls.user)

    def test_str(self):
        """Test Availability string"""
        period = Availability.objects.create(profile=self.profile,
                                             weekday=Availability.SUNDAY,
                                             start_time=Availability.NINE_AM,
                                             end_time=Availability.ONE_PM,
                                             created_by=self.user,
                                             modified_by=self.user)
        self.assertEqual(str(period), 'Sunday 9:00 am - 1:00 pm')
