from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(verbose_name = 'Описание')
    image = models.ImageField(upload_to='shop/')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории')
    slug = models.SlugField(max_length=100, unique=False, verbose_name='URL')
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    time = models.DateField(auto_now_add=True)
    comment = models.TextField()

# class Order(model.Models):
#     user =  model.models.ForeignKey(User, on_delete=models.CASCADE)
    
