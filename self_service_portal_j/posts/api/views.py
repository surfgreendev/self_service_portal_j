from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from self_service_portal_j.posts.api.serializers import PostSerializer
from self_service_portal_j.posts.models import Post


class PostListAPIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
