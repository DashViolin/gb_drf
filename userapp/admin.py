from django.contrib import admin

from userapp import models as userapp_models


@admin.register(userapp_models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "is_active", "date_joined"]
    ordering = ["-date_joined"]
