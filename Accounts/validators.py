from django.core.exceptions import ValidationError
import re


def validate_phone(value):
    if not re.fullmatch(r'^09\d{9}$', value):
        raise ValidationError("Invalid Phone Number!")

