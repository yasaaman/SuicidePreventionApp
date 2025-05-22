from rest_framework import serializers
from .models import UserProfile, UserHealthInfo, UserTrustedContact
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from test2 import settings
import ssl
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend


class UserHealthInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHealthInfo
        exclude = ['user']


class UserTrustedContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrustedContact
        exclude = ['user']


class UserProfileSerializer(serializers.ModelSerializer):
    health_info = UserHealthInfoSerializer(write_only=True)
    trusted_contact = UserTrustedContactSerializer(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'last_name', 'email', 'phone_number', 'password', 'health_info', 'trusted_contact']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        # read_only_fields = ['phone_number']

    def create(self, validated_data):
        health_data = validated_data.pop('health_info')
        trusted_data = validated_data.pop('trusted_contact')
        password = validated_data.pop('password')

        user = UserProfile(**validated_data)
        user.set_password(password)
        user.save()

        UserHealthInfo.objects.create(user=user, **health_data)
        UserTrustedContact.objects.create(user=user, **trusted_data)

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("کاربری با این ایمیل وجود ندارد.")

        if not user.check_password(password):
            raise serializers.ValidationError("رمز عبور اشتباه است.")

        data['user'] = user
        return data


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError("کاربری با این ایمیل وجود ندارد.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = UserProfile.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        reset_url = f"http://your-frontend-url.com/reset-password?uid={uid}&token={token}"
        try:
            send_mail(
                "بازیابی رمز عبور",
                f"برای تغییر رمز عبور، روی لینک زیر کلیک کنید:\n{reset_url}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            print("✅ ایمیل با موفقیت ارسال شد.")
        except Exception as e:
            print("❌ خطا در ارسال ایمیل:", str(e))

class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        try:
            uid = urlsafe_base64_decode(data['uid']).decode()
            user = UserProfile.objects.get(pk=uid)
        except (UserProfile.DoesNotExist, ValueError, TypeError, OverflowError):
            raise serializers.ValidationError("اطلاعات لینک نادرست است.")

        if not default_token_generator.check_token(user, data['token']):
            raise serializers.ValidationError("توکن معتبر نیست یا منقضی شده است.")

        self.user = user
        return data

    def save(self):
        self.user.set_password(self.validated_data['new_password'])
        self.user.save()
