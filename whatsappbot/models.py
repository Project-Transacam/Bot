from django.db import models


class TransactionHistory(models.Model):
    transaction_type_list =(
        ('pay_fees','Pay Fees'),
        ('send_money','send Money'),
        ('cashin','Cashin'),
        ('Cashout','Cashout'),
        )
    transaction_id = models.CharField(max_length=70,primary_key=True)
    amount = models.FloatField(default=0,null=True)
    from_number = models.CharField(max_length=20,null=True)
    to_number = models.CharField(max_length=20,null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    transaction_type = models.CharField(max_length=20,choices=transaction_type_list,default=None)
    