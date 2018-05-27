# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Login(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=30)
    creat_ed = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name