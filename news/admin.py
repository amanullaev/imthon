from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    search_fields = ['posted_at', 'category', 'id']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['title', 'created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)