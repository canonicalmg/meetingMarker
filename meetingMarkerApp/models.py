from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Meeting(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=300, blank=True)
    startTime = models.DateTimeField(default=datetime.now)
    endTime = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title