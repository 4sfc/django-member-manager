"""AvailabilityFormTest class"""

from member_manager.models import Availability
from member_manager.forms.availability import AvailabilityForm
from member_manager.tests.availability_test_case import AvailabilityTestCase


class AvailabilityFormTest(AvailabilityTestCase):
    """Test AvailabilityForm"""

    @classmethod
    def get_form(cls, start, end):
        """Return the form."""
        return AvailabilityForm({'profile': cls.profile.id,
                                 'weekday': Availability.SUNDAY,
                                 'start_time': start,
                                 'end_time': end,
                                 'created_by': cls.user,
                                 'modified_by': cls.user})
