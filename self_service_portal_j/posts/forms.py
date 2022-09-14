from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from self_service_portal_j.posts.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "sub_title", "category", "content", "tags", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-create-post"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_post"
        self.helper.add_input(Submit("submit", _("Speichern")))
