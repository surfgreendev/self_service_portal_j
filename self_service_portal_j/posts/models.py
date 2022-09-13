import os
import sys

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


# Create your models here.
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
    image = models.ImageField(
        _("Cover Image"),
        upload_to="blog/cover_images/",
        height_field=None,
        width_field=None,
        max_length=None,
    )
    content = models.TextField(_("Blog Inhalt"), blank=True, null=True)
    slug = models.SlugField(
        _("Slug"), blank=True, null=True, help_text=_("Titel als Url")
    )
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
        super(Post, self).save(*args, **kwargs)


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
