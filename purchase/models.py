from unicodedata import category
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Purchase(models.Model):
    invoice_date = models.DateField()
    invoice_no = models.CharField(max_length=250)
    from_add = models.CharField(max_length=250)
    delivery_date = models.DateField()
    item_id =   models.CharField(max_length=250)
    item_name = models.CharField(max_length=250)
    model_no = models.CharField(max_length=250)
    quantity = models.IntegerField()
    purchase_price = models.IntegerField()
    discount = models.IntegerField()
