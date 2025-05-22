from rest_framework import serializers
from .models import Music, Video
import re


def extract_drive_id(drive_link):
    """
    Extract Google Drive file ID from the standard share/view URL.
    """
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', drive_link)
    if match:
        return match.group(1)
    return None


class MusicSerializer(serializers.ModelSerializer):
    playable_url_flutter = serializers.SerializerMethodField()
    # playable_url_browser = serializers.SerializerMethodField()

    class Meta:
        model = Music
        fields = ['id', 'title', 'drive_link', 'playable_url_flutter']

    def get_playable_url_flutter(self, obj):
        file_id = extract_drive_id(obj.drive_link)
        if file_id:
            return f"https://drive.google.com/uc?export=download&id={file_id}"
        return None

    # def get_playable_url_browser(self, obj):
    #     file_id = extract_drive_id(obj.drive_link)
    #     if file_id:
    #         return f"https://drive.google.com/file/d/{file_id}/preview"
    #     return None


class VideoSerializer(serializers.ModelSerializer):
    playable_url_flutter = serializers.SerializerMethodField()
    playable_url_browser = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'drive_link', 'playable_url_flutter', 'playable_url_browser']

    def get_playable_url_flutter(self, obj):
        file_id = extract_drive_id(obj.drive_link)
        if file_id:
            return f"https://drive.google.com/uc?export=download&id={file_id}"
        return None

    def get_playable_url_browser(self, obj):
        file_id = extract_drive_id(obj.drive_link)
        if file_id:
            return f"https://drive.google.com/file/d/{file_id}/preview"
        return None
