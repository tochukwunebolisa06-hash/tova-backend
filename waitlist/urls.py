from django.urls import path

from .views import WaitlistJoinView

urlpatterns = [
    path("", WaitlistJoinView.as_view(), name="waitlist-join"),
]
