from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "role", "university", "rating", "is_approved", "created_at"]
    list_editable = ["category", "is_approved"]
    list_filter = ["is_approved", "category", "rating", "university"]
    search_fields = ["name", "quote", "university", "role"]
    ordering = ["-created_at"]