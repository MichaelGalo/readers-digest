from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_created"
    )
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} review of {self.book.title}"
