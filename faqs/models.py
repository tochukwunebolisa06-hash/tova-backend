from django.db import models


class FAQ(models.Model):
    """A published question/answer pair, managed from the Django admin."""

    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(
        default=0, help_text="Lower numbers show first on the FAQs page."
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "created_at"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class FAQQuestion(models.Model):
    """A question a visitor submitted through the 'ask a question' box."""

    question = models.TextField()
    email = models.EmailField(blank=True, help_text="Optional — only if they want a reply.")
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Submitted question"
        verbose_name_plural = "Submitted questions"

    def __str__(self):
        return self.question[:60]
