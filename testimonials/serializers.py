from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    """Used for the public GET list — approved testimonials only."""

    class Meta:
        model = Testimonial
        fields = [
            "id",
            "name",
            "quote",
            "rating",
            "university",
            "category",
            "role",
            "created_at",
        ]


class TestimonialSubmitSerializer(serializers.ModelSerializer):
    """Used for the public submission form. is_approved, category and role are
    never exposed here — every submission starts unapproved as a regular
    'student' review, and an admin can recategorise it during review."""

    class Meta:
        model = Testimonial
        fields = ["id", "name", "quote", "rating", "university"]
        read_only_fields = ["id"]

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Name can't be empty.")
        return value

    def validate_quote(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Review can't be empty.")
        return value

    def validate_university(self, value):
        return (value or "").strip()