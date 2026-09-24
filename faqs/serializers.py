from rest_framework import serializers

from .models import FAQ, FAQQuestion


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "order"]


class FAQQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQQuestion
        fields = ["id", "question", "email", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_question(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Question can't be empty.")
        return value
