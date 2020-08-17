"""AvailabilityInlineFormSetTest class"""

from django.forms.models import inlineformset_factory

from member_manager.forms.availability_inline_formset import (
    AvailabilityInlineFormSet
)
from member_manager.models import Availability
from member_manager.models import Profile
from member_manager.tests.availability_test_case import AvailabilityTestCase


class AvailabilityInlineFormSetTest(AvailabilityTestCase):
    """Test AvailabilityInlineFormSet"""

    @classmethod
    def get_form(cls, start, end):
        """
        Return form.

        :param start int: Start time in military time * 100
        :param end int: End time in military time * 100

        :return form: Form
        """
        formset = inlineformset_factory(Profile, Availability,
                                        formset=AvailabilityInlineFormSet,
                                        exclude=['created', 'modified'])
        form = formset(data={'availability_set-TOTAL_FORMS': '1',
                             'availability_set-INITIAL_FORMS': '0',
                             'availability_set-MAX_NUM_FORMS': '',
                             'availability_set-0-profile': cls.profile.id,
                             'availability_set-0-weekday': Availability.SUNDAY,
                             'availability_set-0-start_time': start,
                             'availability_set-0-end_time': end,
                             'availability_set-0-created_by': cls.user.id,
                             'availability_set-0-modified_by': cls.user.id},
                       instance=cls.profile)
        return form
