from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category
from .scraping import scraping
from django.utils.text import slugify # создание слагов



def index(request):
    for item in scraping():
        obj = Product.objects.create(title=item['name'], description=item['description'],
        image=item['image'], price=item['price'], slug=item['slug']) 
        obj.save()
    return render(request, 'shop/index.html')
