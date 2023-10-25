from . import models
from account.models import User
from django.shortcuts import get_object_or_404
from . import serializers
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly



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
    parser_classes = (MultiPartParser,)
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Categories.
    """
    parser_classes = (MultiPartParser,)
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Comments.
    """
    parser_classes = (MultiPartParser,)
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)