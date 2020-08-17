"""AvailabilityTestCase class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Availability
from member_manager.models import Profile


class AvailabilityTestCase(TestCase):
    """AvailabilityTestCase to test availability periods."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo', email='foo@example.com')
        cls.profile = Profile.objects.create(first_name='foo',
                                             last_name='bar',
                                             email='foo@example.com',
                                             user=cls.user,
                                             created_by=cls.user,
                                             modified_by=cls.user)
    @classmethod
    def get_form(cls, start, end):
        """
        Returns the form.

        :param start int: Start time in military time * 100
        :param end int: End time in military time * 100

        :raises NotImplementedError: Child classes must define it.
        """
        raise NotImplementedError

    @classmethod
    def is_period_valid(cls, start, end):
        """
        Return True if availability period is valid.

        :param start int: Start time in military time * 100
        :param end int: End time in military time * 100

        :return bool: True if form is valid
        """
        form = cls.get_form(start, end)
        return form.is_valid()

    def test_invalid_availability_period(self):
        """Test invalid availability period"""
        self.assertFalse(self.is_period_valid(Availability.NINE_AM,
                                              Availability.ELEVEN_AM))

    def test_valid_availability_period(self):
        """Test valid availability period"""
        self.assertTrue(self.is_period_valid(Availability.NINE_AM,
                                             Availability.ELEVEN_FIFTEEN_AM))
