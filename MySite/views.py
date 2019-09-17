from django.http import HttpResponse, JsonResponse

from .models import Product


def new_product(request):

		if request.method == "POST":
			if request.POST.get('position') and request.POST.get('price'):

				price, position = request.POST['price'], request.POST['position']
				product_ = Product.objects.create(position = position, price = price)
				product_.save()
				return HttpResponse(product_.id)

			else: return HttpResponse ("Bad Date")

		else: return HttpResponse ("Only Post")


def get_product(request):


	if request.method == "GET":

		tmp = []

		if request.GET.get('position') or request.GET.get('price'):
			filter_dict = {}

			if request.GET.get('position'): filter_dict['position'] = request.GET['position']
			if request.GET.get('price'): filter_dict['price'] = request.GET['price']

			product_s = Product.objects.filter(**filter_dict)

			tmp = [p_.to_dict() for p_ in product_s]

		else:
			tmp = [p_.to_dict() for p_ in Product.objects.all()]

		return JsonResponse(tmp, safe = False)
