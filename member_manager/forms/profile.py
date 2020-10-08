"""ProfileForm class"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from member_manager.models.profile import Profile


class ProfileForm(forms.ModelForm):
    """ProfileForm class inherits custom save"""

    def clean_phone(self):
        """Clean phone field"""
        data = self.cleaned_data['phone']
        if len(data) != 10:
            raise ValidationError(_('Enter a valid 10-digit phone number.'))
        if not data.isdigit():
            raise ValidationError(_('Enter only numbers--e.g., 1234567890.'))
        return data

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'pronouns', 'email', 'phone',
                  'join_reason', 'how_heard', 'how_heard_other']
