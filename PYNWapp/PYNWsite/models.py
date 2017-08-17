# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    event_date = models.DateTimeField('event date')
    description = models.TextField()

    def __str__(self):
        return self.name

    def is_future(self):
       return self.event_date > timezone.now()

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Category')

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
