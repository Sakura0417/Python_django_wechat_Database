from django.db import models


# Create your models here.

class JDcommodityInfo (models.Model):
    productname = models.CharField(max_length=256)
    productimg = models.CharField(max_length=128)
    productprice = models.DecimalField(max_digits=5,decimal_places=2)

class ToutiaoIInfo (models.Model):
    title = models.CharField(max_length=64)
    auther = models.CharField(max_length=16)
    date = models.DateField()
    img = models.CharField(max_length=128)
    linkaddress = models.CharField(max_length=128)
