from django.db import models
from sympy import false, true
import datetime

from employee.models import Employee

# Create your models here.
class Salary(models.Model):
    emp_id = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    nic = models.CharField(max_length=250)
    bank = models.CharField(max_length=250)
    pay_period = models.CharField(max_length=250)
    tax_no = models.CharField(max_length=250)
    basic_salary = models.IntegerField()
    dedcutions = models.IntegerField()
    net_salary = models.IntegerField()