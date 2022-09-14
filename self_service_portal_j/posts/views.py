import logging

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView, View

from self_service_portal_j.posts.forms import PostCreateForm
from self_service_portal_j.posts.models import Post, PostCategory

logger = logging.getLogger("__name__")


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        logger.debug("Request received %s" % request.user)
        post = get_object_or_404(Post, pk=self.kwargs["pk"])

        logger.debug("Requested post is %s" % post.title)
        return render(request, "posts/post_detail.html", {"post": post})


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
