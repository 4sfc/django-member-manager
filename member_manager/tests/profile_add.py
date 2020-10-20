"""ProfileAddViewTest class"""

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from member_manager.models.profile import Profile
from member_manager.views.profile_add import ProfileAddView


class ProfileAddViewTest(TestCase):
    """ProfileAddViewTest tests the ProfileAddView class"""

    @classmethod
    def setUpTestData(cls):
        request_factory = RequestFactory()
        cls.request = request_factory.get('/member_manager/profile')
        cls.request.user = AnonymousUser()
        cls.request.session = {}
        cls.data = {'first_name': 'foo', 'last_name': 'bar',
                    'email': 'fb@example.com', 'phone': '0987654321'}

    def test_form_valid(self):
        """Tests form_valid"""
        view_i = ProfileAddView(success_url='/availability',
                                **{'request': self.request})
        form_class = view_i.get_form_class()
        form = form_class(data=self.data)
        self.assertTrue(view_i.form_valid(form))
        foo_profile = Profile.objects.get(email='fb@example.com')
        self.assertEqual(self.request.session['profile_id'], foo_profile.id)
