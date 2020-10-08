"""ProfileFormTest class"""

from django.test import TestCase

from member_manager.forms.profile import ProfileForm


class ProfileFormTest(TestCase):
    """ProfileFormTest tests ProfileForm"""

    @classmethod
    def setUpTestData(cls):
        cls.data = {'first_name': 'foo', 'last_name': 'bar',
                    'email': 'fb@example.com'}

    def test_long_phone(self):
        """Test invalid long phone"""
        data = self.data.update({'phone': '12345678900'})
        form = ProfileForm(data=data)
        self.assertFalse(form.is_valid())

    def test_nondigit_phone(self):
        """Test invalid nondigit phone"""
        data = self.data.update({'phone': '123abc7890'})
        form = ProfileForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_phone(self):
        """Test valid nondigit phone"""
        data = self.data
        for number in ['9999999999', '0000000000']:
            data['phone'] = number
            form = ProfileForm(data=data)
            self.assertTrue(form.is_valid())
