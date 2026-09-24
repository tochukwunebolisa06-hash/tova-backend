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
