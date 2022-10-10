from rest_framework import serializers

from self_service_portal_j.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "status",
            "title",
            "sub_title",
            "category",
            "image",
            "author",
            "content",
            "published_on",
            "created_on",
            "updated_on",
        ]
