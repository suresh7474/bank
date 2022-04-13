from django.db import models

# Create your models here.
#from customer.models import Cust as Cust

class AccountInfo(models.Model):
    accNo=models.IntegerField('account_no')
    accBal = models.FloatField('account_bal')
    accType = models.CharField('account_type',max_length=50)
    accremarks = models.CharField('account_remarks',max_length=50)
 #   customers = models.ForeignKey(Cust, on_delete=models.CASCADE,related_name='account')
    class Meta:
        db_table='Account_Info'
