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

    def test_post_create(self):
        title = fake.text(max_nb_chars=20)
        sub_title = fake.text(max_nb_chars=20)
        content = fake.text(max_nb_chars=100)
        tags = "tag1, tag2"

        # Setup post data
        data = {
            "title": title,
            "sub_title": sub_title,
            "content": content,
            "tags": tags,
        }

        # Send post request
        result = self.client.post(reverse("posts:create"), data=data, follow=True)

        # Check 200 status code
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, "posts/post_list.html")

        # Test success message
        self.assertIn("alert alert-dismissible alert-success", result.content.decode())

        # Test if object has been created in the database
        self.assertEqual(title, Post.objects.filter(title=title).first().title)
        self.assertEqual(sub_title, Post.objects.filter(title=title).first().sub_title)
        self.assertEqual(content, Post.objects.filter(title=title).first().content)

        self.assertEqual(Post.objects.count(), 2)
