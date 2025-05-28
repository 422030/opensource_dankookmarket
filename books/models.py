from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    CONDITION_CHOICES = [
        ('new', '새 책'),
        ('good', '양호'),
        ('fair', '보통'),
        ('poor', '사용감 있음'),
    ]
    STATUS_CHOICES = [
        ('available', '판매중'),
        ('reserved', '예약중'),
        ('sold', '거래완료'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    description = models.TextField()
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.seller.username}"

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='interests')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # 중복 찜 방지

class Transaction(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='transaction')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    status = models.CharField(max_length=20, choices=Book.STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.buyer.username}"

