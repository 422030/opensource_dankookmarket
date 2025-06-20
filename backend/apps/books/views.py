from rest_framework import viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Book, Interest, Transaction
from .serializers import BookSerializer, InterestSerializer, TransactionSerializer
from django.contrib.auth.models import User

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(seller=User.objects.first())
        #serializer.save(seller=self.request.user)  # ✅ seller 저장

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Interest.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='check')
    def check_interest(self, request):
        user = request.user
        book_id = request.query_params.get('book_id')

        if not book_id:
            return Response({'error': 'book_id query param required'}, status=400)

        exists = Interest.objects.filter(user=user, book_id=book_id).exists()
        return Response({'interested': exists})

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
