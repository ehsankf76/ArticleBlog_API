from .views import UserViewSet
from rest_framework.routers import DefaultRouter



urlpatterns = []
router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
urlpatterns += router.urls