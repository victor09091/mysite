# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created')

admin.site.register(Product,ArticleAdmin)
# Register your models here.
