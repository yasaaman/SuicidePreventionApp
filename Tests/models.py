from django.db import models
from django.conf import settings
from Accounts.models import UserTrustedContact


class PsychologicalTestResult(models.Model):
    RISK_LEVELS = [
        ('low', 'کم‌خطر'),
        ('medium', 'متوسط'),
        ('high', 'پرخطر'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='test_results')
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)

    def __str__(self):
        return f"{self.risk_level}"
