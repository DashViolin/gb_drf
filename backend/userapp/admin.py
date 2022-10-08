from django.contrib import admin

from userapp.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "is_staff", "is_superuser", "date_joined"]
    ordering = ["id"]
