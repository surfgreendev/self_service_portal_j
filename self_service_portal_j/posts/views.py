from django.shortcuts import render
from django.views.generic import CreateView, ListView

from self_service_portal_j.posts.forms import PostCreateForm
from self_service_portal_j.posts.models import Post, PostCategory


class PostCreateView(CreateView):
    model = Post
    # fields = ["status", "title", "sub_title", "content", "tags"]
    form_class = PostCreateForm


class PostCategoryCreateView(CreateView):
    model = PostCategory
    fields = ["title", "description"]


class PostListView(ListView):
    model = Post
    queryset = Post.objects.select_related("category").all()
