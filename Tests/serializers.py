from rest_framework import serializers
from .models import PsychologicalTestResult


class PsychologicalTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalTestResult
        fields = ['id', 'risk_level']
