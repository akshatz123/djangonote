from builtins import super

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Tag(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.label

    def _get_unique_slug(self):
        slug = slugify(self.label)
        unique_slug = slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Tag, self).save(*args, **kwargs)


class Note(models.Model):
    label = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    tags = models.ForeignKey('Tag', related_name='notes', blank=True, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
