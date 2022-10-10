from django.test import Client, TestCase
from django.utils.text import slugify
from faker import Faker

from self_service_portal_j.posts.models import Post, PostCategory

fake = Faker()


class TestPostModel(TestCase):
    def setUp(self):
        self.title = fake.text(max_nb_chars=20)

        self.post = Post.objects.create(title=self.title)

    def tearDown(self):
        pass

    def test_assert(self):
        self.assertEqual("Hello World", "Hello World")

    def test_post_created(self):
        self.assertEqual(self.post.pk, Post.objects.get(id=self.post.pk).pk)
        self.assertEqual(self.post.title, Post.objects.get(id=self.post.pk).title)

    def test_post_str_method(self):
        self.assertEqual(
            str(self.post), "{} - {}".format(self.post.pk, self.post.title)
        )

    def test_post_slugify(self):
        slug = slugify(self.title)
        self.assertEqual(slug, self.post.slug)


class TestPostViews(TestCase):
    pass
