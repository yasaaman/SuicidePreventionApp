from rest_framework import viewsets
from .models import Music, Video
from .serializers import MusicSerializer, VideoSerializer
from rest_framework.permissions import AllowAny


class MusicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [AllowAny]


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [AllowAny]
