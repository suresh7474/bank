from django.contrib import admin
from  .models import Employee,Address
# Register your models here.
#from .models import Cust
admin.site.register(Employee)
admin.site.register(Address)