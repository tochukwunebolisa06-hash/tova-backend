from rest_framework import serializers

from .models import WaitlistEntry


class WaitlistEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitlistEntry
        fields = ["id", "email", "name", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_email(self, value):
        return value.strip().lower()
