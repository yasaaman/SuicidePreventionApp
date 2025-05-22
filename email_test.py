import django
import os
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test2.settings")
django.setup()


send_mail(
    'Test Email',
    'This is a test email from Django.',
    'umi65997@gmail.com',
    ['y.peykhosh@gmail.com'],  # ← اینجا ایمیل واقعی مقصد رو بزن
    fail_silently=False,
)
