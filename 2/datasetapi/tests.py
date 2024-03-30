from django.test import TestCase 
from django.urls import reverse

from rest_framework.test import APIClient 
from rest_framework import status

# Create your tests here.

class StockTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_stock_list(self):
        pass

    def test_stock_create(self):
        pass

    def test_stock_partial_update(self):
        pass
    
    def test_stock_full_update(self):
        pass

    def test_stock_delete(self):
        pass

    def test_valid_stock_category(self):
        pass

    def test_invalid_stock_category(self):
        pass

    def test_duplicate_product_name(self):
        pass
