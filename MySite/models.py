from django.db import models

class Product (models.Model):

	position = models.CharField(max_length = 20)
	price = models.FloatField()

	def to_dict(self):
		return {
			'price' : self.price,
			'position' : self.position,
		}
