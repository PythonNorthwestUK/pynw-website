# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Event, Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)



 
