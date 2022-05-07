from django.db import models
import uuid

# Create your models here.
from account.models import Account


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=10, )
    date = models.DateField()
    reference_no = models.TextField(max_length=50)
    total_amount = models.FloatField()
    remark = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
