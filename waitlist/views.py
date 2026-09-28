from django.conf import settings
from django.db import IntegrityError
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WaitlistEntry
from .serializers import WaitlistJoinSerializer

ALREADY_JOINED = {"detail": "You're already on the waitlist.", "already_joined": True}


class WaitlistJoinView(APIView):
    """POST /api/waitlist/

    Body: { "email": "..." } or { "phone": "..." } (or both), plus an
    optional "name". Re-submitting an email/phone that's already on the list
    returns a friendly "already joined" response instead of an error.
    """

    def post(self, request):
        serializer = WaitlistJoinSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        phone = serializer.validated_data.get("phone")
        name = serializer.validated_data.get("name", "")

        lookup = Q()
        if email:
            lookup |= Q(email=email)
        if phone:
            lookup |= Q(phone=phone)

        if WaitlistEntry.objects.filter(lookup).exists():
            return Response(ALREADY_JOINED, status=status.HTTP_200_OK)

        try:
            WaitlistEntry.objects.create(email=email, phone=phone, name=name)
        except IntegrityError:
            # Two identical requests raced each other — the other one won.
            return Response(ALREADY_JOINED, status=status.HTTP_200_OK)

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