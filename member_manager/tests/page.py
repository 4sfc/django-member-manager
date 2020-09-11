"""PageTest class"""

from django.contrib.auth.models import User
from django.test import TestCase

from member_manager.models import Page


class PageTest(TestCase):
    """Test Page model"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='foo', email='foo@example.com')
        page_content = "Thank you for your interest"
        cls.page = Page.objects.create(title='Thank You',
                                       content=page_content,
                                       slug="thank-you",
                                       created_by=cls.user,
                                       modified_by=cls.user)

    def test_str(self):
        """Test Page string"""
        self.assertEqual(str(self.page), 'Thank You')
