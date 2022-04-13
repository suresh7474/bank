from django.db import models,connection

# Create your models here.
from django.http import JsonResponse

class Employee(models.Model):
    ename = models.CharField('emp_name', max_length=50)
    eage = models.IntegerField('emp_age')


#e1 = Employee(id=1,ename='AAAA',eage=20)

class Address(models.Model):
    city = models.CharField('city',max_length=50)
    pin = models.IntegerField('pin')
    employee = models.ManyToManyField(Employee,related_name='address')


#Address(id=101,city='Pune',pin=238834)

#Cust(id=1,cname='AAAA',cage=34)



'''
    Address --- id city pin cust
            coln  -- id city pin
            
            
         adr.cust --- Customer    
    Cust
            -- id cname cage address
            --id cname cage address_id
            
        cust.address -- Address
'''