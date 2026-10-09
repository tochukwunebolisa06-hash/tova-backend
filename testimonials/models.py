from django.db import models


class Testimonial(models.Model):
    """A testimonial submitted by a visitor. Published automatically unless hidden in admin."""

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    CATEGORY_CHOICES = [
        ("student", "Student / Member"),
        ("leader", "Pastor / Church leader"),
    ]

    name = models.CharField(max_length=120)
    quote = models.TextField(max_length=600)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    university = models.CharField(max_length=150, blank=True, default="")
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default="student",
        help_text="Which column of the Home page this appears in.",
    )
    role = models.CharField(
        max_length=150,
        blank=True,
        default="",
        help_text="Shown under the name, e.g. 'Senior Pastor, Lagos'. Falls back to the university if blank.",
    )
    is_approved = models.BooleanField(
        default=True,
        help_text="Untick to hide a testimonial from the public site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} ({self.rating}\u2605)"