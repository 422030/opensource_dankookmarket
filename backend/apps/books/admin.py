from django.contrib import admin
from .models import Book, Interest, Transaction

admin.site.register(Book)
admin.site.register(Interest)
admin.site.register(Transaction)
