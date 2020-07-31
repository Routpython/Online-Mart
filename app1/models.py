from django.db import models

class Productdetails(models.Model):
    idno=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30,unique=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="images/")
    pdate=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=60)
    
class Usermodel(models.Model):
    no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20)


