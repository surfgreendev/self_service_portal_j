import os
import sys

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _
from taggit.managers import TaggableManager

from self_service_portal_j.posts.managers import PostManager

User = get_user_model()


class PostComment(models.Model):
    title = models.CharField(_("Titel"), max_length=250)
    comment = models.TextField(_("Kommentar"))

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Kommentar")
        verbose_name_plural = _("Kommentare")
        ordering = ["-created_on"]

    def __str__(self):
        return "{} - {}".format(self.pk, self.title)


class PostCategory(models.Model):
    title = models.CharField(_("Titel"), max_length=250)
    description = models.TextField(_("Bschreibung"), blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post Kagegorie")
        verbose_name_plural = _("Post Kategorien")
        ordering = ["-created_on"]

    def __str__(self):
        return "{} - {}".format(self.pk, self.title)


class Post(models.Model):
    """Post model needs the following fileds:
    * status (DRAFT, PUBLISHED)
    * author --> Foreign Key User
    * title
    * sub_title
    * content
    * slug
    * image
    * published_on
    * created_on
    * updated_on
    """

    class PostStatus(models.TextChoices):
        DRAFT = "DRAFT", _("Entwurf")
        PUBLISHED = "PUBLISHED", _("Veroeffentlicht")

    status = models.CharField(
        _("Status"), max_length=50, choices=PostStatus.choices, default=PostStatus.DRAFT
    )
    title = models.CharField(_("Titel"), max_length=250)
    sub_title = models.CharField(_("Untertitel"), max_length=250, blank=True, null=True)
    category = models.ForeignKey(
        PostCategory,
        verbose_name=_("Post Kategorie"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        _("Cover Image"),
        upload_to="blog/cover_images/",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User, verbose_name=_("Autor"), on_delete=models.CASCADE, blank=True, null=True
    )
    content = models.TextField(_("Blog Inhalt"), blank=True, null=True)
    slug = models.SlugField(
        _("Slug"), blank=True, null=True, help_text=_("Titel als Url")
    )
    tags = TaggableManager()
    published_on = models.DateTimeField(
        _("Veroeffentlich am"),
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created_on"]
        get_latest_by = ["-created_on"]

    def __str__(self):
        # return str(self.pk) + "-" + self.title
        return "{} - {}".format(self.pk, self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if self.status == self.PostStatus.PUBLISHED:
            self.published_on = timezone.now()

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:list")

    objects = PostManager()


# Create your models here.
class PostImages(models.Model):
    post = models.ForeignKey(
        Post, verbose_name=_("Post"), on_delete=models.CASCADE, blank=True, null=True
    )
    title = models.CharField(_("Titel"), max_length=250)
    alt_text = models.TextField(_("Bschreibung"), blank=True, null=True)

    image = models.ImageField(
        _("Bild"),
        upload_to="blog/images",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Post Bild")
        verbose_name_plural = _("Post Bilder")

    def __str__(self):
        return "{} - {}".format(self.pk, self.title)


"""
class PostCategory(models.Model):
    pass

class PostComment(models.Model):
    pass

class PostSEOMeta(models.Model):
    pass

class PostImage(models.Model):
    pass
uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
"""
