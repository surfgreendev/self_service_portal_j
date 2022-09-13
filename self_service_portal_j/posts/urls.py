from django.urls import path

from self_service_portal_j.posts.views import PostCreateView

app_name = "posts"

urlpatterns = [
    path("create/", view=PostCreateView.as_view(), name="create"),
]
