from rest_framework.generics import ListAPIView, CreateAPIView

from .models import FAQ, FAQQuestion
from .serializers import FAQSerializer, FAQQuestionSerializer


class FAQListView(ListAPIView):
    """GET /api/faqs/  — published FAQs, in admin-defined order."""

    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.filter(is_published=True)


class FAQAskView(CreateAPIView):
    """POST /api/faqs/ask/  { "question": "...", "email": "..." (optional) }"""

    queryset = FAQQuestion.objects.all()
    serializer_class = FAQQuestionSerializer
