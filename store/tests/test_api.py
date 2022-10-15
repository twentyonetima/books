from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price='10.01',
                                          author_name='Test Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price='200.02',
                                          author_name='Test Author 2')
        self.book_3 = Book.objects.create(name='Test book 3', price='300.03',
                                          author_name='Test Author 2')
        self.book_4 = Book.objects.create(name='Test Author book 4', price='300.03',
                                          author_name='Test Author 4')

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2,
                                          self.book_3, self.book_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'price': 300.03})
        serializer_data = BookSerializer([self.book_3,
                                          self.book_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 2'})
        serializer_data = BookSerializer([self.book_3,
                                          self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
