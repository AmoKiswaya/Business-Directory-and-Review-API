from django.db import models
from django.conf import settings

class Review(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} Stars") for i in range(1, 6)]
    )
    comment = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('business', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f"Review {self.rating}★ by {self.user} on {self.business}"

    @property
    def stars(self):
        return "⭐" * self.rating + "☆" * (5 - self.rating) 


