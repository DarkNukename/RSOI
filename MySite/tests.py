from django.test import TestCase
from MySite.models import Product
# Create your tests here.

class ProductTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		Product.objects.create(price = '777' , position = 'Milk')


	def test_colum_name(self):
		_product = Product.objects.get(id = 1)
		colum_name0 = _product._meta.get_field('position').verbose_name
		colum_name1 = _product._meta.get_field('price').verbose_name
		self.assertEqual(colum_name0, "position")
		self.assertEqual(colum_name1, "price")


	def test_name_lenght(self):
		__product = Product.objects.get(id = 1)
		lenght0 = __product._meta.get_field("position").max_length
		self.assertEqual(lenght0, 20)

	def test_new_product(self):
		data = { 'position' : 'Hawk', 'price' : 7.20, }

		response = self.client.post(
			path = '/my-site/new_product/',
			data = data
		)

		self.assertEqual(response.status_code, 200)
		self.assertNotIn(b'Bad Date', response.content)
		self.assertNotIn(b'Only Post', response.content)


	def test_get_product(self):
		response = self.client.get('/my-site/new_product/?price=7.20&position=Hawk')
		self.assertEqual(response.status_code, 200)
		self.assertNotIn(b'Bad Date', response.content)
		self.assertNotIn(b'Only Get', response.content)
