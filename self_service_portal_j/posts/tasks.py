from celery.utils.log import get_task_logger
from django.core.mail import send_mail

from config import celery_app
from self_service_portal_j.posts.models import Post

logger = get_task_logger(__name__)


@celery_app.task()
def send_list_of_blog_posts():
    posts = Post.objects.all()
    post_string = ""
    for post in posts:
        logger.info("Blog Post %s" % post)
        post_string += "Post: {} \n".format(post.title)

    send_mail(
        "List of posts",
        "Here is the list of posts\n " + post_string,
        "from@example.org",
        ["to@example.org"],
        fail_silently=False,
    )
