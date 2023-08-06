from django.db import models
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

# Create your models here.
class License(models.Model):
    sdk_nr=models.IntegerField(max_length=50)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.name


class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    license=models.ForeignKey(License, related_name='license', on_delete=models.CASCADE)
    expiry_date=models.DateField()
    def __str__(self):
        return self.name
    
    @property
    def remain_days(self):
        days= self.expiry_date - date.today()
        days_stripped= str(days).split(' ')[0]
        days_int= int(days_stripped)
        if days_int <= 90:
            print(f'EMAIL WAS SENT')
            return HttpResponse('Email sent successfully!')
        return days_int