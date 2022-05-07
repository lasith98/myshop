from django.db import models


class Account(models.Model):
    account_no = models.CharField(max_length=25)
    account_name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=50)
    barch_code = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
