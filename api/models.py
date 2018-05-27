# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    describe = models.CharField(max_length=500, default='')
    price = models.FloatField()
    isDelete = models.BooleanField(default=False)
    # creat_ed = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(default=timezone.now)   #modify

    class Meta:
        ordering = ('created',)

# Create your models here.
