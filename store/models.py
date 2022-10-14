from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField('Name', max_length=255)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)