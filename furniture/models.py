from django.db import models

# Create your models here.


class furniture(models.Model):
    model=models.CharField(max_length=200 , verbose_name='krovat')
    colos=models.CharField(max_length=150 , verbose_name='aq')
    strana=models.TextField(verbose_name='Uzbekistan')
    price=models.TextField(verbose_name='10 m')
    quality=models.CharField(max_length=200 , verbose_name='derevo')