from django.contrib import admin

from .models import WaitlistEntry


@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    list_display = ["email", "name", "created_at"]
    search_fields = ["email", "name"]
    ordering = ["-created_at"]
