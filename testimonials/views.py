from rest_framework.generics import ListAPIView, CreateAPIView

from .models import Testimonial
from .serializers import TestimonialSerializer, TestimonialSubmitSerializer


class TestimonialListView(ListAPIView):
    """GET /api/testimonials/ returns approved testimonials, newest first."""

    serializer_class = TestimonialSerializer

    def get_queryset(self):
        return Testimonial.objects.filter(is_approved=True)


class TestimonialSubmitView(CreateAPIView):
    """POST /api/testimonials/submit/
    { "name": "...", "quote": "...", "rating": 5, "university": "..." (optional) }

    New testimonials are published immediately. To hide one, untick
    is_approved in Django admin (Testimonials, then Testimonials).
    """

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSubmitSerializer