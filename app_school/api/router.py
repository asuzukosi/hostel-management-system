from .viewsets import SchoolAdminViewset, SchoolViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("admin", SchoolAdminViewset, basename="school admin")
router.register("", SchoolViewSet, basename="school")


urlpatterns = router.urls