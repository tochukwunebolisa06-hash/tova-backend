from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WaitlistEntry
from .serializers import WaitlistEntrySerializer


class WaitlistJoinView(APIView):
    """POST /api/waitlist/  { "email": "...", "name": "..." (optional) }"""

    def post(self, request):
        email = (request.data.get("email") or "").strip().lower()
        if not email:
            return Response(
                {"detail": "An email address is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        existing = WaitlistEntry.objects.filter(email=email).first()
        if existing:
            # Already on the list — treat as a friendly success, not an error.
            return Response(
                {"detail": "You're already on the waitlist.", "already_joined": True},
                status=status.HTTP_200_OK,
            )

        serializer = WaitlistEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "You're on the waitlist!", "already_joined": False},
            status=status.HTTP_201_CREATED,
        )


class WaitlistCountView(APIView):
    """GET /api/waitlist/count/  — total number of people on the waitlist.

    Adds WAITLIST_COUNT_OFFSET (an optional env var, defaults to 0) on top
    of the real database count, in case you ever want the public number to
    reflect interest gathered before this counter existed. Leave it
    unset/0 to show the exact database count.
    """

    def get(self, request):
        real_count = WaitlistEntry.objects.count()
        offset = getattr(settings, "WAITLIST_COUNT_OFFSET", 0)
        return Response({"count": real_count + offset})