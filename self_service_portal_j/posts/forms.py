from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import gettext as _

from self_service_portal_j.posts.models import Post, PostComment


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


class PostCommentCreateForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ["post", "title", "comment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-create-comment"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_comment"
        self.helper.add_input(Submit("submit", _("Speichern")))
