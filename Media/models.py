from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=255)
    drive_link = models.URLField(verbose_name="Google Drive Link")

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    drive_link = models.URLField(verbose_name="Google Drive Link")

    def __str__(self):
        return self.title
