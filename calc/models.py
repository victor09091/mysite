# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    creat_ed = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name