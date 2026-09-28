from django.db import models


class WaitlistEntry(models.Model):
    """Someone on the waitlist. They join with an email, a phone number, or both.

    Both columns are nullable + unique so many people can have "no phone" (or
    "no email") without colliding on an empty string. The check constraint
    guarantees every row has at least one way to reach the person.
    """

    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="International format, e.g. +2348012345678.",
    )
    name = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Waitlist entry"
        verbose_name_plural = "Waitlist entries"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(email__isnull=False) | models.Q(phone__isnull=False),
                name="waitlist_email_or_phone_required",
            ),
        ]

    def save(self, *args, **kwargs):
        # Blank strings (e.g. from the admin form) must be stored as NULL so
        # the unique constraints and the either-or check behave correctly.
        self.email = (self.email or "").strip().lower() or None
        self.phone = (self.phone or "").strip() or None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email or self.phone or f"Entry {self.pk}"