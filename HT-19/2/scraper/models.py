from django.db import models


# Create your models here.

STORIES_CHOICES = (
    ("askstories", "ASK"),
    ("showstories", "SHOW"),
    ("newstories", "NEW"),
    ("jobstories", "JOB"),
)

class Choice(models.Model):
    name = models.CharField(max_length=40, choices=STORIES_CHOICES, default="new")

    def __str__(self):
        return self.name


class Ask(models.Model):
    by = models.TextField(default=None, null=True)
    item_id = models.IntegerField(primary_key=True)
    score = models.TextField(default=None, null=True)
    time = models.TextField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    item_type = models.TextField(default=None, null=True)
    descendants = models.TextField(default=None, null=True)
    kids = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)

class New(models.Model):
    by = models.TextField(default=None, null=True)
    item_id = models.IntegerField(primary_key=True)
    score = models.TextField(default=None, null=True)
    time = models.TextField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    item_type = models.TextField(default=None, null=True)
    descendants = models.TextField(default=None, null=True)
    kids = models.TextField(default=None, null=True)
    text = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)


class Show(models.Model):
    by = models.TextField(default=None, null=True)
    item_id = models.IntegerField(primary_key=True)
    score = models.TextField(default=None, null=True)
    time = models.TextField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    item_type = models.TextField(default=None, null=True)
    descendants = models.TextField(default=None, null=True)
    kids = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)


class Job(models.Model):
    by = models.TextField(default=None, null=True)
    item_id = models.IntegerField(primary_key=True)
    score = models.TextField(default=None, null=True)
    time = models.TextField(default=None, null=True)
    title = models.TextField(default=None, null=True)
    item_type = models.TextField(default=None, null=True)
    url = models.TextField(default=None, null=True)
