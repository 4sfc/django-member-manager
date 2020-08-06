"""AvailabilityForm class"""

from django import forms
from django.utils.translation import gettext as _

from member_manager.models.availability import Availability
from member_manager.utils import MemberManagerUtils as mmu


class AvailabilityForm(forms.ModelForm):
    """AvailabilityForm adds a custom clean function"""

    INVALID_PRD = _('Start to end must be a %(hours)s hour and %(minutes)s '
                    'minute period.')
    MISSING_END_POINT = _('Each entry must have start and end times.')
    VALID_HRS = 2
    VALID_MNS = 15

    class Meta:
        fields = ['profile', 'weekday', 'start_time', 'end_time']
        model = Availability

    def clean(self):
        """
        Clean form data and verify start to end times are a valid period.

        :raises forms.ValidationError: Invalid start-to-end period
        """
        cleaned_data = super().clean()
        try:
            valid = mmu.valid_period(cleaned_data.get('start_time', None),
                                     cleaned_data.get('end_time', None),
                                     self.VALID_HRS, self.VALID_MNS)
        except TypeError:
            raise forms.ValidationError(
                self.INVALID_PRD, code='invalid_period',
                params={'hours': self.VALID_HRS, 'minutes': self.VALID_MNS}
            )
        if not valid:
            raise forms.ValidationError(
                self.INVALID_PRD, code='invalid_period',
                params={'hours': self.VALID_HRS, 'minutes': self.VALID_MNS}
            )
