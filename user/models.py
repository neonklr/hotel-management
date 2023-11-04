from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, primary_key=True, unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
