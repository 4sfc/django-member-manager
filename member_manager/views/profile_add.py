"""ProfileAddView class"""

from django.forms import modelform_factory

from common_files.views.timestamp import TimestampCreateView
from member_manager.forms.profile import ProfileForm
from member_manager.models.profile import Profile


class ProfileAddView(TimestampCreateView):
    """ProfileAddView"""

    form_class = modelform_factory(Profile, form=ProfileForm,
                                   fields=['first_name', 'last_name',
                                           'pronouns', 'email', 'phone',
                                           'join_reason', 'how_heard',
                                           'how_heard_other'])
    template_name = 'member_manager/profile_add_form.html'

    def form_valid(self, form):
        """Save valid form and add profile_id to session."""
        redirect = super().form_valid(form)
        self.request.session['profile_id'] = self.object.id
        return redirect
