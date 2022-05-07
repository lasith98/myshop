from django.db import models


# Create your models here.

class BalanceSheet(models.Model):
    balance_sheet_id = models.CharField(max_length=10)
    date = models.DateField()
    liabilities = models.FloatField()
    equity = models.FloatField()
    asset = models.FloatField()
