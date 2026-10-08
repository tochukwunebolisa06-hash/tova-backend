from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle

from .models import ChurchPartner, PartnershipInquiry
from .serializers import ChurchPartnerSerializer, PartnershipInquirySerializer


class ChurchPartnerListView(ListAPIView):
    """GET /api/partners/  — published church partners, in admin-defined order."""

    serializer_class = ChurchPartnerSerializer

    def get_queryset(self):
        return ChurchPartner.objects.filter(is_published=True)


class PartnershipInquiryView(CreateAPIView):
    """POST /api/partners/inquire/
    { "church_name": "...", "contact_name": "...", "email": "...",
      "phone": "..." (optional), "message": "..." (optional) }

    Rate limited (see 'inquiry' in REST_FRAMEWORK settings) to curb spam.
    """

    queryset = PartnershipInquiry.objects.all()
    serializer_class = PartnershipInquirySerializer
    throttle_classes = [AnonRateThrottle, ScopedRateThrottle]
    throttle_scope = "inquiry"