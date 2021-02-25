from rest_framework.routers import DefaultRouter

from .views import SchoolViewSet

router = DefaultRouter()

router.register(prefix='api/v1/schools',
                viewset=SchoolViewSet, basename='school')

urlpatterns = router.urls
