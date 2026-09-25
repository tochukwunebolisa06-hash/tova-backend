from django.urls import path

from .views import WaitlistJoinView, WaitlistCountView

urlpatterns = [
    path("", WaitlistJoinView.as_view(), name="waitlist-join"),
    path("count/", WaitlistCountView.as_view(), name="waitlist-count"),
]