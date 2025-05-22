from django.contrib import admin
from .models import UserProfile, UserHealthInfo, UserTrustedContact


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'phone_number')
    search_fields = ('name', 'last_name', 'email', 'phone_number')
    list_filter = ('name', 'last_name')


@admin.register(UserHealthInfo)
class UserHealthInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'sleep_hours', 'economic_status')
    search_fields = ('user__name', 'user__last_name')
    list_filter = ('economic_status',)
    raw_id_fields = ('user',)


@admin.register(UserTrustedContact)
class UserTrustedContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'trusted_name', 'trusted_lastname', 'trusted_phone_number')
    search_fields = ('user__name', 'name', 'last_name')
    raw_id_fields = ('user',)
