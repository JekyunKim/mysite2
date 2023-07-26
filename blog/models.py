from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    # draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]

    def __str__(self):
        return self.title
