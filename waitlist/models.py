from django.db import models


class WaitlistEntry(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Waitlist entry"
        verbose_name_plural = "Waitlist entries"

    def __str__(self):
        return self.email
