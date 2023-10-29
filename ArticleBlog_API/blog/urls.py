from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('categories/<slug:slug>/articles', views.CategoryArticleListAPIView.as_view(), name='category-article-list'),
    path('authors/<slug:slug>/articles', views.AuthorArticleListAPIView.as_view(), name='author-article-list'),
    path('articles/<slug:article_slug>/average-rating/', views.ArticleAverageRatingView.as_view(), name='article-average-rating'),
]
router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('comments', views.CommentViewSet, basename='comments')
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)