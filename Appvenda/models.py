from django.db import models
import random

# Create your models here.

def set_default_category():
    return Category.objects.get_or_create(name="outros")[0]
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, default=set_default_category)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET(set_default_category))
    lot = models.CharField(max_length=100, default= str(random.randint(1000, 9999)))
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    stock = models.CharField(max_length=100, default=0)

    
    def __str__(self):
        return self.name
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.client.name} - {self.product.name}"
    
