# apps/groups/urls.py

from django.urls import path
from .views import create_group_buy

urlpatterns = [
    path('create/', create_group_buy),
]
