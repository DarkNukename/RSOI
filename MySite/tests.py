from django.test import TestCase
from MySite.models import Product
# Create your tests here.

class ProductTest(TeatCase)
	def setData(cls):
		Product.object.create(position = "Milk", price = "777")

	def test_colum_name(self)
		__product = Product.objects.get(id = 1)
		colum_name0 = product0._meta.get_field('position').verbose_name
		colum_name1 = product0._meta.get_field('price').verbose_name
		self.assertEqual(colum_name0, "product")
		self.assertEqual(colum_name1, "price")


	def test_name_lenght(self)
		__product = Product.objects.get(id = 1)
		lenght0 = __product._meta.get_field("position").max_length
		lenght1 = float(__product._meta.get_field("price").max_length)
		self.assertEqual(lenght0, "product")
		self.assertEqual(lenght1, "price")
