from django.urls import path

from .views import ChurchPartnerListView, PartnershipInquiryView

urlpatterns = [
    path("", ChurchPartnerListView.as_view(), name="partner-list"),
    path("inquire/", PartnershipInquiryView.as_view(), name="partner-inquire"),
]