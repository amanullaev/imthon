from .models import *
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'created_at')


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'text', 'posted_at', 'category')