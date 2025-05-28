from django.db import models
from django.contrib.auth.models import User

class GroupBuyRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    is_matched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class GroupBuyMatch(models.Model):
    group_request = models.ForeignKey(GroupBuyRequest, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
