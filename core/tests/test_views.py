from django.test import TestCase, Client
from django.urls import reverse
from core.models import Book, OrderBook, Order, BillingAddress
import json


class TestViews(TestCase):

    def test_products_GET(self):
        pass
