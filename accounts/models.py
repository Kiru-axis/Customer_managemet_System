from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=18,null=True)
    email=models.EmailField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ("Indoor","Indoor"),
        ("Outdoor","Outdoor"),
    )
    name = models.CharField(max_length=70,null=True)
    price = models.FloatField(null=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ("Pending","Pending"),
        ("Put for delivery","Out for delivery"),
       ( "Delivered","Delivered")
    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product= models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=300,null=True,choices=STATUS)

    def __str__(self):
        return f"{self.product} , {self.customer}"