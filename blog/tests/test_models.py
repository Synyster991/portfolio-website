from django.test import TestCase
from django.utils import timezone
import datetime

from blog import models


def sample_post():
    return models.Post.objects.create(
        title='Django',
        body="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has 
        been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type 
        and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap 
        into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the 
        release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
        software like Aldus PageMaker including versions of Lorem Ipsum""",
        link='www.example.com',
        image='',
        post_date=datetime.datetime.now(tz=timezone.utc)
    )


def sample_comment(post_fk):
    return models.Comment.objects.create(
        person='Smith',
        body='Lorem Ipsum is simply dummy text',
        post_date=datetime.datetime.now(tz=timezone.utc),
        post=post_fk
    )


class BlogModelTest(TestCase):
    """Test models associate with Blog"""
    def test_post_listing(self):
        """Test posts listing"""
        post = sample_post()
        sample_comment(post)

        pulled_post = models.Post.objects.get(title='Django')
        pulled_comment = models.Comment.objects.get(post=pulled_post)

        self.assertEqual(pulled_comment.post, pulled_post)

    def test_post_string_representation(self):
        """Test post str"""
        post = sample_post()
        self.assertEqual(str(post), 'Django')

    def test_post_summary(self):
        """Test post summary of the body"""
        post = sample_post()
        self.assertEqual(len(post.summary()), 150)

    def test_comment_string_representation(self):
        """Test Comment str"""
        pulled_post = sample_post()
        pulled_comment = sample_comment(pulled_post)

        self.assertEqual(str(pulled_comment), 'Lorem Ipsum is simply dummy text')

