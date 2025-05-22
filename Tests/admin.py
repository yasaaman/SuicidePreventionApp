from django.contrib import admin
from .models import PsychologicalTestResult


@admin.register(PsychologicalTestResult)
class PsychologicalTestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'risk_level']
    search_fields = ['user__email', 'risk_level']
    list_filter = ['risk_level']
