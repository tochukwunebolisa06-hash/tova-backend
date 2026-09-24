from django.contrib import admin

from .models import FAQ, FAQQuestion


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "order", "is_published", "updated_at"]
    list_editable = ["order", "is_published"]
    search_fields = ["question", "answer"]
    ordering = ["order", "created_at"]


@admin.register(FAQQuestion)
class FAQQuestionAdmin(admin.ModelAdmin):
    list_display = ["question", "email", "is_answered", "created_at"]
    list_editable = ["is_answered"]
    search_fields = ["question", "email"]
    list_filter = ["is_answered"]
    ordering = ["-created_at"]
