from django.contrib import admin
from .models import License,Customer,Admin
# Register your models here.
admin.site.register(Customer)
admin.site.register(License)