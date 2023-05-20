from rest_framework import generics, pagination
from .models import Book
from .serializers import BookSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        return Book.objects.all().order_by("id")
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'