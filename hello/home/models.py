#model is about what we use to create database 
from django.db import models
from django import forms
#makemigrations - create changes and store in a file
#migrate - apply the peding changes created my makemigrations
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone =models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self): #it shows name in admin panel instead of object 1,2,3
        return self.name
    
class login(models.Model):
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    
class Register(models.Model):
    username = models.CharField(max_length=122, unique=True)
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.username



