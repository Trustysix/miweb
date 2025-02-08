from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        Product.objects.create(name="Test Product", quantity=10, date="2023-10-01")

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.quantity, 10)
        self.assertEqual(product.date, "2023-10-01")

    def test_product_quantity_update(self):
        product = Product.objects.get(name="Test Product")
        product.quantity += 5
        product.save()
        updated_product = Product.objects.get(name="Test Product")
        self.assertEqual(updated_product.quantity, 15)

    def test_product_deletion(self):
        product = Product.objects.get(name="Test Product")
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(name="Test Product")