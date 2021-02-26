from rest_framework import generics
from books.models import Book
from cars.models import Car
from .serializers import BookSerializer, CarSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CarAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer