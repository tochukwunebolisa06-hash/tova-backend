from django.db import models


class Testimonial(models.Model):
    """A testimonial submitted by a visitor. Only shown on the site once approved."""

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    name = models.CharField(max_length=120)
    quote = models.TextField(max_length=600)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    is_approved = models.BooleanField(
        default=False,
        help_text="Only approved testimonials appear on the public site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} ({self.rating}\u2605)"
