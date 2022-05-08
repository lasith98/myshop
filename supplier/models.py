from unicodedata import category
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    item_name = models.CharField(max_length=250)
    date = models.DateField()
