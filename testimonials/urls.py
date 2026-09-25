from django.urls import path

from .views import TestimonialListView, TestimonialSubmitView

urlpatterns = [
    path("", TestimonialListView.as_view(), name="testimonial-list"),
    path("submit/", TestimonialSubmitView.as_view(), name="testimonial-submit"),
]
