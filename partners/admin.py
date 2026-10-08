from django.contrib import admin

from .models import ChurchPartner, PartnershipInquiry


@admin.register(ChurchPartner)
class ChurchPartnerAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "order", "is_published", "updated_at"]
    list_editable = ["order", "is_published"]
    search_fields = ["name", "location", "quote", "author"]
    ordering = ["order", "created_at"]


@admin.register(PartnershipInquiry)
class PartnershipInquiryAdmin(admin.ModelAdmin):
    list_display = ["church_name", "contact_name", "email", "phone", "is_contacted", "created_at"]
    list_editable = ["is_contacted"]
    list_filter = ["is_contacted"]
    search_fields = ["church_name", "contact_name", "email", "phone", "message"]
    ordering = ["-created_at"]