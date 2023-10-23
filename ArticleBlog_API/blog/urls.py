from django.urls import path
from .views import AuthorArticleListAPIView, CategoryArticleListAPIView, ArticleViewSet, CategoryViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('categories/<slug:slug>/articles', CategoryArticleListAPIView.as_view(), name='category-article-list'),
    path('authors/<slug:slug>/articles', AuthorArticleListAPIView.as_view(), name='author-article-list'),
]
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('comments', CommentViewSet, basename='comments')
urlpatterns += router.urls