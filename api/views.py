from rest_framework import generics
from book.models import Book
from .serializers import BookSerializer

class BookAPIView (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer