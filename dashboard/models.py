from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models.base import Model  

class giftVoucher(models.Model):
    amout50 = models.IntegerField(null =True,blank=True)
    amout30 = models.IntegerField(null =True,blank=True)
    amout20 = models.IntegerField(null =True,blank=True)
    dateTimeGift = models.DateTimeField()
    complete = models.BooleanField(default=False)
     

    def __str__(self):
        return str(self.dateTimeGift)
