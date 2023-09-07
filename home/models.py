from django.db import models

# Create your models here.
class registration_data (models.Model):
    name=models.CharField(max_length=40)
    phone=models.IntegerField()
    email=models.EmailField()
    sex=models.CharField(max_length=50, default="0")
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    Languages=models.CharField(max_length=100)
    uname=models.CharField(max_length=100, default="0")
    role=models.CharField(max_length=100, default="0")

    
class admin_data (models.Model):
    uname=models.CharField(max_length=100, default="0")
    password=models.CharField(max_length=40, default="0")
    

class registration_create(models.Model):
    uname=models.CharField(max_length=100, default="0")
    password=models.CharField(max_length=40, default="0")



class workers_data( models.Model):
    name=models.CharField(max_length=40,default="0")
    image_face = models.ImageField(upload_to="images", db_column="image")
    field=models.CharField(max_length=100)
    experience=models.IntegerField()
    exp_cnf=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    image_work1 = models.ImageField(upload_to="images", db_column="photo1",default="0")
    image_work2 = models.ImageField(upload_to="images", db_column="photo2",default="0")
    image_work3 = models.ImageField(upload_to="images", db_column="photo3",default="0")
    uname=models.CharField(max_length=100, default="0")

    