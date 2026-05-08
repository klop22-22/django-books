from django.shortcuts import render
from rest_framework import generics
from .serializers import BooksSerializer, AuthorsSerializer
from .models import Book, Author


class BooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class AuthorsAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer