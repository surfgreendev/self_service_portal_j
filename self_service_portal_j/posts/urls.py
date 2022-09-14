from django.urls import path

from self_service_portal_j.posts.views import (
    PostCategoryCreateView,
    PostCreateView,
    PostListView,
)

app_name = "posts"

urlpatterns = [
    path("create/", view=PostCreateView.as_view(), name="create"),
    path(
        "category/create/",
        view=PostCategoryCreateView.as_view(),
        name="category-create",
    ),
    path("overview/", view=PostListView.as_view(), name="list"),
]
