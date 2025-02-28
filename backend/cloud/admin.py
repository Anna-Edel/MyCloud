from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CloudUser, CloudFile

@admin.register(CloudUser)
class CloudUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'storage_path')}),
    )

@admin.register(CloudFile)
class CloudFileAdmin(admin.ModelAdmin):
    list_display = ('original_name', 'user', 'size', 'upload_date', 'last_download_date')