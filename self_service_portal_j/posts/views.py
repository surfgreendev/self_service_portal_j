from django.shortcuts import render
from django.views.generic import CreateView

from self_service_portal_j.posts.models import Post, PostCategory


class PostCreateView(CreateView):
    model = Post
    fields = ["status", "title", "sub_title", "content", "tags"]


class PostCategoryCreateView(CreateView):
    model = PostCategory
    fields = ["title", "description"]
