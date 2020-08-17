"""MemberManagerUtilsTest class"""

from django.test import TestCase

from member_manager.utils import MemberManagerUtils


class MemberManagerUtilsTest(TestCase):
    """Test MemberManagerUtils"""

    def test_invalid_period(self):
        """Test invalid period"""
        self.assertFalse(MemberManagerUtils.valid_period(900, 1100, 2, 15))

    def test_valid_period(self):
        """Test valid period"""
        self.assertTrue(MemberManagerUtils.valid_period(1300, 1515, 2, 15))
