from django.db import models


class Post(models.Model):
    """Post Model"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    post_date = models.DateTimeField(blank=True)

    def __str__(self):
        return "{}".format(self.title)

    def summary(self):
        return "{}".format(self.body[:150])


class Comment(models.Model):
    person = models.CharField(max_length=255)
    body = models.TextField()
    post_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.body[:150])
