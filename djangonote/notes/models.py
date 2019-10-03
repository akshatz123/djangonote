from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Note(models.Model):
	label = models.CharField(max_length=200)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	user = 	models.ForeignKey(User,on_delete=models.CASCADE)
	tags = models.ManyToManyField('Tag', related_name='notes', blank=True)

	def __str__(self):
		return self.label

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
		super().save(*args, **kwargs)
