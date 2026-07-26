from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ("username", "role")
    list_editable = ("role",)
    search_fields = ("username",)
