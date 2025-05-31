from django.db import models
from django.contrib.auth.models import User
from apps.books.models import Book

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1~5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
