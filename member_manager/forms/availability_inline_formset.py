'''AvailabilityInlineFormSet class'''

from django import forms
from django.forms.models import BaseInlineFormSet

from member_manager.forms.availability import AvailabilityForm as af
from member_manager.utils import MemberManagerUtils as mmu

class AvailabilityInlineFormSet(BaseInlineFormSet):
    '''AvailabilityInlineFormSet has a custom clean function'''

    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                start = form.cleaned_data.get('start_time', None)
                end = form.cleaned_data.get('end_time', None)
                try:
                    valid = mmu.valid_period(start, end, af.VALID_HRS,
                                             af.VALID_MNS)
                except TypeError:
                    valid = False
                if not valid:
                    raise forms.ValidationError(
                        af.INVALID_PRD, code='invalid_period',
                        params={'hours': af.VALID_HRS, 'minutes': af.VALID_MNS},
                    )
