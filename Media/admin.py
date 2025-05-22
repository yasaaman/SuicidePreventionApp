from django.contrib import admin
from .models import Music, Video


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'drive_link')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'drive_link')
