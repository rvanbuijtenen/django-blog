# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
	class Meta:
		verbose_name = ("Comment")

	author = models.CharField(null=False, max_length=128)
	content = models.CharField(null=False, max_length=10000)
	date = models.DateTimeField(null=False, default=timezone.now)

class Post(models.Model):
	class Meta:
		verbose_name = ('Blog Post')

	title = models.CharField(null=False, max_length=128)
	author = models.CharField(null=False, max_length=128)
	content = models.CharField(null=False, max_length=10000)
	date = models.DateTimeField(null=False, default=timezone.now)
	comments = models.ManyToManyField(Comment)

