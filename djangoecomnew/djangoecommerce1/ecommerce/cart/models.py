from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.products.name

    def subtotal(self):
        return self.quantity*self.products.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    order_status = models.CharField(max_length=30, default="pending")
    delivery_status = models.CharField(max_length=30, default="pending")
    noofitems = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class Account(models.Model):
    acctype=models.CharField(max_length=20)
    accno=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return self.accno

