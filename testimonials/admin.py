from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "is_approved", "created_at"]
    list_editable = ["is_approved"]
    list_filter = ["is_approved", "rating"]
    search_fields = ["name", "quote"]
    ordering = ["-created_at"]
