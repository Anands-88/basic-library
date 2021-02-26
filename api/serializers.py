from rest_framework import serializers
from books.models import Book
from cars.models import Car

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','subtitle','author','isbn','price','id')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name','company','model','price','id')