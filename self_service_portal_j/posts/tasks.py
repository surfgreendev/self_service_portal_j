from celery.utils.log import get_task_logger

from config import celery_app
from self_service_portal_j.posts.models import Post

logger = get_task_logger(__name__)


@celery_app.task()
def send_list_of_blog_posts():
    posts = Post.objects.all()
    for post in posts:
        logger.info("Blog Post %s" % post)
