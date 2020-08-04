from django.db import models


class Job(models.Model):
    """Job model"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    source_link = models.CharField(max_length=255, blank=True)
    preview_link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "{}".format(self.title)

    def summary(self):
        """Create short summary from the description"""
        return "{}".format(self.description[:100])


class Achievement(models.Model):
    """Achievement model"""
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    issued_by = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.title)

    def summary(self):
        """Create short summary from the body"""
        return "{}".format(self.body[:100])


class Guest(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    alcohol = models.CharField(max_length=255)

    def __str__(self):
        return "{} ({}) - {}".format(self.name, self.email, self.alcohol)