# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')

admin.site.register(Person,ArticleAdmin)