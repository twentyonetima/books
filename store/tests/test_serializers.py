from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price='10.01')
        book_2 = Book.objects.create(name='Test book 2', price='200.02')
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': book_1.name,
                'price': book_1.price,
            },
            {
                'id': book_2.id,
                'name': book_2.name,
                'price': book_2.price,
            }
        ]
        self.assertEqual(expected_data, data)