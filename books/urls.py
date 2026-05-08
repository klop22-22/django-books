from django.urls import path
from . import views
from .views import BooksAPIView, AuthorsAPIView


app_name = 'books'


urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='booklist'),
    path('authors/', AuthorsAPIView.as_view(), name='authorlist')
]