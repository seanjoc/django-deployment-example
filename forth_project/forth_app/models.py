from django.db import models

# Create your models here.
class User(models.Model):
    ufirst_name = models.CharField(max_length=100)
    ulast_name = models.CharField(max_length=100)
    uemail = models.EmailField(max_length=100,unique=True)
