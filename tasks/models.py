from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["is_done", "created"]
