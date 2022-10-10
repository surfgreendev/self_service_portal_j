from django.test import Client, TestCase
from django.urls import reverse
from faker import Faker

from self_service_portal_j.posts.models import Post, PostCategory

fake = Faker()


class TestPostViews(TestCase):
    def setUp(self):
        self.title = fake.text(max_nb_chars=20)
        self.post = Post.objects.create(title=self.title)
        self.client = Client()

    def test_post_list(self):
        result = self.client.get(reverse("posts:list"))
        self.assertEqual(result.status_code, 200)

        self.assertInHTML("<h1>Post Listing</h1>", result.content.decode())
        self.assertIn("te_create_post_btn", result.content.decode())
        self.assertInHTML("<h5>{}</h5>".format(self.title), result.content.decode())
        self.assertTemplateUsed(result, "posts/post_list.html")

    def test_post_detail(self):
        result = self.client.get(reverse("posts:detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(result.status_code, 200)
        self.assertInHTML("<h1>{}</h1>".format(self.title), result.content.decode())
        self.assertTemplateUsed(result, "posts/post_detail.html")
        self.assertIn("te_create_form", result.content.decode())
