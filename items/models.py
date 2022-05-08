from unicodedata import category
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
