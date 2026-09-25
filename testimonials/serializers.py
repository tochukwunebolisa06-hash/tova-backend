from rest_framework import serializers

from .models import Testimonial


class TestimonialSerializer(serializers.ModelSerializer):
    """Used for the public GET list — approved testimonials only."""

    class Meta:
        model = Testimonial
        fields = ["id", "name", "quote", "rating", "created_at"]


class TestimonialSubmitSerializer(serializers.ModelSerializer):
    """Used for the public submission form. is_approved is never exposed here —
    every submission starts unapproved and waits for admin review."""

    class Meta:
        model = Testimonial
        fields = ["id", "name", "quote", "rating"]
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
