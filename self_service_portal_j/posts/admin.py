from django.contrib import admin

# Register your models here.
from self_service_portal_j.posts.models import Post, PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "published_on"]
