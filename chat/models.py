from django.db import models
from django.contrib.auth import get_user_model
from ecom.models import Customer
from datetime import *
User = get_user_model()
DEFAULT_EXAM_ID = 1
class Room(models.Model):
    nameRoom = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    content = models.CharField(max_length=100000,default='No Message', editable=False)
    timestamp =  models.DateTimeField(auto_now_add=True,null=True,blank=True)
    onl = models.BooleanField(default=False)
    def __str__(self):      
        return self.nameRoom.username
 
import datetime
import re 
import datetime
class Message(models.Model):
    
    author = models.ForeignKey(User,related_name=  "author_messages",on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    content = models.CharField(max_length=100000)
    timestamp =  models.DateTimeField(auto_now_add=True)
 
    def __str__(self):      
        return self.author.username


    def time(self):
       
        x=((datetime.datetime.now()-self.timestamp))
        # print("type:",type(datetime.datetime(x)))
        # print("ago:",x.strftime("%H:%M:%S"))
        #  
        # # for i in x:
        # #     if i == "d":

        # #     print(" ",i)
        
        print("x:",x.total_seconds())
        x=x.total_seconds()
        if x<60:
            return str(int(x))+"s"
        elif x<3600:
            return str(int(x//60))+"m"
        elif x<86400:
            return str(int(x//3600)) +"h"
        elif x<2592000:
            return str(int(x//86400)) +"day"
        elif x<31104000:
            return str(int(x//259200)) +"month"
        else:
            return str(int(x//31104000)) +"year"
         
       

    def last_10_messages(roomName):
        count =int(Message.objects.filter(room = roomName).count())
        if count<=10:
            count =10
        return Message.objects.filter(room = roomName).order_by('timestamp').all()[count-10:count]

    
 
    
 
    
