from .viewsets import SchoolViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", SchoolViewSet, basename="school")

urlpatterns = router.urls