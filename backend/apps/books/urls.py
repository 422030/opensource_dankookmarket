from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, InterestViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'interests', InterestViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
