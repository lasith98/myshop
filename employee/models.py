from django.db import models
from sympy import false, true
import datetime

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    occupation = models.CharField(max_length=250)
