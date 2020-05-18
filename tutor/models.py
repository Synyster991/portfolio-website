from django.db import models


class Course(models.Model):
    """Model for storing courses"""
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)


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

# TODO
# QandA:
# 	title
# 	person
# 	body
# 	source_link (blank=True)
#
# Comment:
# 	person
# 	body
# 	post (FK)