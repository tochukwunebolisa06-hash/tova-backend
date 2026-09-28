import os
import re

from rest_framework import serializers


def normalize_phone(raw):
    """Turn whatever the visitor typed into E.164 (+<country code><number>).

    Accepted inputs:
      +234 801 234 5678   -> +2348012345678
      00234 801 234 5678  -> +2348012345678
      0801 234 5678       -> +2348012345678  (national format, uses the default
                             country code below)

    The default country code for national-format numbers comes from the
    WAITLIST_DEFAULT_COUNTRY_CODE env var (defaults to 234). Set it to an
    empty value to require the country code on every number.

    Returns None for blank input. Raises ValidationError for anything invalid.
    """
    raw = (raw or "").strip()
    if not raw:
        return None

    if re.search(r"[^\d\s\-\.\(\)\+]", raw) or "+" in raw[1:]:
        raise serializers.ValidationError(
            "Phone number can only contain digits, spaces, dashes, brackets and a leading +."
        )

    digits = re.sub(r"\D", "", raw)
    default_cc = re.sub(r"\D", "", os.environ.get("WAITLIST_DEFAULT_COUNTRY_CODE", "234"))

    if raw.startswith("+"):
        pass  # already international
    elif digits.startswith("00"):
        digits = digits[2:]
    elif digits.startswith("0") and default_cc:
        digits = default_cc + digits[1:]
    else:
        raise serializers.ValidationError(
            "Please include your country code, e.g. +234 801 234 5678."
        )

    if digits.startswith("0") or not 8 <= len(digits) <= 15:
        raise serializers.ValidationError("Please enter a valid phone number.")

    return "+" + digits


class WaitlistJoinSerializer(serializers.Serializer):
    """Input for POST /api/waitlist/ — an email, a phone number, or both.

    Deliberately not a ModelSerializer: the model's unique validators would
    turn "already on the list" into a 400, but the API treats that as a
    friendly success (handled in the view).
    """

    email = serializers.EmailField(required=False, allow_blank=True, allow_null=True)
    phone = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, max_length=40
    )
    name = serializers.CharField(required=False, allow_blank=True, max_length=150)

    def validate_email(self, value):
        return (value or "").strip().lower() or None

    def validate_phone(self, value):
        return normalize_phone(value)

    def validate(self, attrs):
        if not attrs.get("email") and not attrs.get("phone"):
            raise serializers.ValidationError(
                {"detail": "Please enter an email address or a phone number."}
            )
        return attrs