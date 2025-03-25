from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser):
    ...
    
class sklad(models.Model):
    num_sklad = models.PositiveIntegerField()
    
class product(models.Model):
    name = models.CharField(max_length=30)
    num = models.PositiveIntegerField() 
    quantity = models.PositiveIntegerField() 
    sklad =models.ForeignKey(sklad, related_name="products", on_delete = models.CASCADE)

class buy(models.Model):
    product = models.ForeignKey(product, verbose_name="buy", on_delete=models.CASCADE)
    product = models.ForeignKey(ApiUser, verbose_name="buy", on_delete=models.CASCADE)