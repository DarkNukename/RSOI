from django.urls import include, path

from .views import new_product, get_product

urlpatterns = [
	path('new_product/', new_product),
	path('get_product/', get_product),

]
