from django.db import models

# Create your models here.


#homepage top picks
class Homemenu(models.Model):
    ProductName = models.CharField(max_length=50)
    ProductPrice = models.IntegerField(max_length=50)
    Description = models.TextField()

#users
class User(models.Model):
    UserName = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=20)
    PhoneNumber = models.IntegerField(max_length=12)
    Location = models.CharField(max_length=20)
  

#orders
class Orders(models.Model):
    UserId = models.IntegerField(max_length=12)
    ProductId = models.IntegerField(max_length=12)
    Quantity = models.IntegerField(max_length=12)
    Status = models.CharField(max_length=20)



    