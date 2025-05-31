from rest_framework import serializers
from .models import Book, Interest, Transaction

class BookSerializer(serializers.ModelSerializer):
    seller_username = serializers.ReadOnlyField(source='seller.username', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Interest
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    buyer_username = serializers.ReadOnlyField(source='buyer.username')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Transaction
        fields = '__all__'
