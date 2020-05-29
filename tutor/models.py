from django.db import models


class Course(models.Model):
    """Model for storing courses"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)
    course_color = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "{}".format(self.title)

    def summary(self):
        """Print summary of the body"""
        return "{}...".format(self.body[:174])


class Video(models.Model):
    """Model for storing videos. One to many relationships with Course"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)
    source_link = models.CharField(max_length=255, blank=True)
    video_link = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)


class PostQA(models.Model):
    """Post for the Q&A"""
    title = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    body = models.TextField()
    source_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}".format(self.title)

    def summary(self):
        """Short text from body"""
        return "{}...".format(self.body[:250])


class CommentQA(models.Model):
    """Model for commenting on QA post"""
    person = models.CharField(max_length=255)
    body = models.TextField()
    post = models.ForeignKey(PostQA, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.post.title, self.person)
