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
