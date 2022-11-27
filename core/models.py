from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    registered_network_list = (
        ('mtn',"MTN"),
        ('orange',"ORANGE"),
        )
    username = models.CharField(max_length=100, blank=True,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,null=True)
    phone = models.CharField(max_length=20,verbose_name='Phone Number',primary_key=True)
    pin = models.CharField(max_length=20,verbose_name='Pin')
    Account_balance = models.FloatField(default=0.0,null=True,verbose_name='Account Balance')
    Account_number = models.CharField(max_length=10,unique=True,null=True)
    registered_telegram = models.BooleanField(default=False,null=True)
    registered_whatsapp = models.BooleanField(default=False,null=True)
    telegram_transactions = models.ForeignKey(to="telegrambot.TransactionHistory",on_delete=models.CASCADE,null=True,related_name="telegram_trans")
    whatsapp_transactions = models.ForeignKey(to="whatsappbot.TransactionHistory",on_delete=models.CASCADE,null=True,related_name="whatsapp_trans")
    user_network = models.CharField(max_length=25,choices=registered_network_list,default=registered_network_list[0])


