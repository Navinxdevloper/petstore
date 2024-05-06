from django.db import models

class Pet(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    M='Male'
    F='Female'
    GENDER=[(M,'Male'),(F,'Female')]
    gender=models.CharField(max_length=10,choices=GENDER)
    breed=models.CharField(max_length=50)
    age=models.IntegerField()
    price=models.FloatField(default=0.0)
    species=models.CharField(max_length=50)
    description=models.CharField(max_length=80)
    pet_image=models.ImageField(null=True,blank=True,upload_to="images/")

class Customer(models.Model):
    name=models.CharField(max_length=50)
    emailId=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    contactNo=models.IntegerField()

class CartModel(models.Model):
    pid=models.ForeignKey(Pet,on_delete=models.CASCADE)
    emailId=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    totalPrice=models.FloatField(default=0.0)

class AdminModel(models.Model):
    adminEmailId=models.CharField(primary_key=True,max_length=50)
    adminpassword=models.CharField(max_length=50)

class Orders(models.Model):
    orderId=models.AutoField(primary_key=True)
    emailId=models.CharField(max_length=100)
    ordernumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phoneno=models.BigIntegerField()
    totalbillamount=models.FloatField(default=0.0)

class Payment(models.Model):
    emailId=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    amount_paid=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    created_st=models.DateTimeField(auto_now=True)


