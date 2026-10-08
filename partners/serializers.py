from rest_framework import serializers

from .models import ChurchPartner, PartnershipInquiry


class ChurchPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChurchPartner
        fields = [
            "id",
            "name",
            "subtitle",
            "location",
            "logo_url",
            "quote",
            "author",
            "role",
            "rating",
            "order",
        ]


class PartnershipInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipInquiry
        fields = ["id", "church_name", "contact_name", "email", "phone", "message"]
        read_only_fields = ["id"]

    def validate_church_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Please enter your church or ministry name.")
        return value

    def validate_contact_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Please enter your name.")
        return value

    def validate_phone(self, value):
        return (value or "").strip()

    def validate_message(self, value):
        return (value or "").strip()