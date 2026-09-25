from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Testimonial
from .serializers import TestimonialSerializer, TestimonialSubmitSerializer


class TestimonialListView(ListAPIView):
    """GET /api/testimonials/  — approved testimonials, newest first."""

    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(is_approved=True)


class TestimonialSubmitView(CreateAPIView):
    """POST /api/testimonials/submit/  { "name": "...", "quote": "...", "rating": 5 }

    Always creates an unapproved testimonial — it won't show on the site
    until an admin approves it in Django admin (Testimonials \u2192 Testimonials).
    """

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSubmitSerializer
