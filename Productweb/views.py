from django.http import HttpResponse
from django.shortcuts import render
from Productweb.models import Products
from Productweb.models import Categories

# Create your views here.

def home(request):
    productsData = Products.objects.all()
    # obj = Products.objects.get()
    # ProductsImage = obj.ProductsImage
    # context = {'products': obj}
    return render(request, 'products/productlist.html', {'data':productsData})
def details(request):
    productsData = Products.objects.all ()
    return render(request, 'products/details.html', {'data': productsData})