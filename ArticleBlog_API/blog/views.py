from . import models
from account.models import User
from django.shortcuts import get_object_or_404
from . import serializers
from rest_framework import viewsets
from rest_framework import generics



class CategoryArticleListAPIView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        category = self.kwargs['slug']
        return models.Article.objects.filter(category__slug=category)
    
class AuthorArticleListAPIView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer

    def get_queryset(self):
        author = self.kwargs['slug']
        return models.Article.objects.filter(author__slug=author)

class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Articles.
    """
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = 'slug'


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Categories.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Comments.
    """
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer