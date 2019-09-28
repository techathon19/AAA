from django.db import models

# Create your models here.


#homepage top picks
class homemenu(models.Model):
    TeaName = models.CharField(max_length=50)
    TeaPrice = models.IntegerField(max_length=50)
    description = models.TextField()

#users
class user(models.Model):
    UserName = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=20)
    PhoneNumber = models.IntegerField(max_length=12)

#real enucard
class menucard(models.Model):
    TeaName = models.CharField(max_length=50)
    TeaPrice = models.IntegerField(max_length=50)
    description = models.TextField()    

#orders
class Orders(models.Model):
    Order_TeaName =  models.CharField(max_length=50)
    TeaPrice = models.IntegerField(max_length=50)

#to find users pattern    
class UserPattern(models.Model):
    User_Id =  models.IntegerField(max_length=50)
    Order_tea = models.CharField(max_length=50)
    Date = models.DateField(auto_now_add=True)


    