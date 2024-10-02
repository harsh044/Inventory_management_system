from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_descriptiom = models.CharField(max_length=500)
    product_category = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name