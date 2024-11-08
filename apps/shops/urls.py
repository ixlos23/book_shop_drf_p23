from django.urls import path

from shops.views import BookListAPIView, CountryListAPIView, BookDetailAPIView

urlpatterns = [
    path('country', CountryListAPIView.as_view()),
    path('books', BookListAPIView.as_view(), name='book-list'),
    path('books/<str:slug>', BookDetailAPIView.as_view(), name='book-detail'),
]
