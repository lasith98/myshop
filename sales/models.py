from django.db import models
from sympy import false, true
import datetime

# Create your models here.
class Sales(models.Model):
    customer = models.CharField(max_length=250)
    date = models.DateField()
    due_date = models.DateField()
    address = models.CharField(max_length=450)
    item_name = models.CharField(max_length=250)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.IntegerField()
