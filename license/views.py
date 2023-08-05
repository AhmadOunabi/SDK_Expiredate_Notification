from django.shortcuts import render
from .models import License,Admin,Customer
from datetime import date

from django.http import HttpResponse
# Create your views here.

def license_reminder(request):
    customers=Customer.objects.all()
    return render(request,'home.html',{'customers':customers})



