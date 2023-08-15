from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from datetime import datetime
from rest_framework.views import APIView


class All_Create_News(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class All_Create_Category(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class Detail_News(APIView):
    def get(self, request, *args, **kwargs):
        news = get_object_or_404(News, id=kwargs['id'])
        serializers = NewsSerializers(news)
        return Response(serializers.data)


class UpdateNews(APIView):
    def patch(self, request, *args, **kwargs):
        news = get_object_or_404(News, id=kwargs['id'])
        serializer = NewsSerializers(news, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteNews(APIView):
    def delete(self, request, *args, **kwargs):
        news = get_object_or_404(News, id=kwargs['id'])
        news.delete()
        return Response({'msg':'deleted'})


class Detail_Category(APIView):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        serializers = CategorySerializers(category)
        return Response(serializers.data)


class UpdateCategory(APIView):
    def patch(self, request, *args, **kwargs):
        category = get_object_or_404(News, id=kwargs['id'])
        serializer = CategorySerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteCategory(APIView):
    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs['id'])
        category.delete()
        return Response({'msg':'deleted'})


class Get_News_By_Category(APIView):
    def get(self, request, *args, **kwargs):
        # news_all = News.objects.all()
        news = get_object_or_404(News, category=kwargs['id'])
        serializers = NewsSerializers(news, many=True)
        return Response(serializers.data)


# class All_Todo(APIView):
#     def get(self, request, *args, **kwargs):
#         all_todo = Todo.objects.all()
#         serializers = TodoSerializers(all_todo, many=True)
#         return Response(serializers.data)