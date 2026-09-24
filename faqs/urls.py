from django.urls import path

from .views import FAQListView, FAQAskView

urlpatterns = [
    path("", FAQListView.as_view(), name="faq-list"),
    path("ask/", FAQAskView.as_view(), name="faq-ask"),
]
