from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, ListView

from self_service_portal_j.posts.forms import PostCreateForm
from self_service_portal_j.posts.models import Post, PostCategory


class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    success_message = _("Blog Post erfolgreich erstellt.")


class PostCategoryCreateView(CreateView):
    model = PostCategory
    fields = ["title", "description"]


class PostListView(ListView):
    model = Post
    queryset = Post.objects.select_related("category").all()
