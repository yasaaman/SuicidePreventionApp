from rest_framework.routers import DefaultRouter
from .views import MusicViewSet, VideoViewSet

router = DefaultRouter()
router.register('music', MusicViewSet)
router.register('videos', VideoViewSet)

urlpatterns = router.urls
