from django.db import models


class ChurchPartner(models.Model):
    """A church partnership shown in the Home page carousel."""

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(max_length=120)
    subtitle = models.CharField(
        max_length=120,
        blank=True,
        default="",
        help_text="Optional second line under the name, e.g. the city.",
    )
    location = models.CharField(max_length=150, blank=True, default="")
    logo_url = models.URLField(
        max_length=500,
        blank=True,
        default="",
        help_text="Link to the church's logo image (PNG/SVG). Leave blank for a placeholder.",
    )
    quote = models.TextField(max_length=700)
    author = models.CharField(
        max_length=150,
        help_text="Who the quote is from, e.g. the church name.",
    )
    role = models.CharField(
        max_length=150,
        blank=True,
        default="",
        help_text="e.g. Lead Pastor & Church Leadership Team",
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers show first in the carousel."
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "created_at"]
        verbose_name = "Church partner"
        verbose_name_plural = "Church partners"

    def __str__(self):
        return self.name


class PartnershipInquiry(models.Model):
    """Submitted through the 'Join Partnership' form on the Home page."""

    church_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, default="")
    message = models.TextField(max_length=1000, blank=True, default="")
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Partnership inquiry"
        verbose_name_plural = "Partnership inquiries"

    def __str__(self):
        return f"{self.church_name} — {self.contact_name}"