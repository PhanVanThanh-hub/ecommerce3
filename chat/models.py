from django.db import models
from django.contrib.auth import get_user_model
from ecom.models import Customer

User = get_user_model()

class Room(models.Model):
    nameRoom = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):      
        return self.nameRoom.username


class Message(models.Model):
     
    author = models.ForeignKey(User,related_name=  "author_messages",on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    content = models.CharField(max_length=100000)
    timestamp =  models.DateTimeField(auto_now_add=True)

    def __str__(self):      
        return self.author.username

    def last_10_messages(roomName):
        print("1231")
        print(roomName)
        print("lalala")
        count =int(Message.objects.filter(room = roomName).count())
        print("aaaaaaaaaaaaa")
        print("count:",count)
        if count<=10:
            count =10
        return Message.objects.filter(room = roomName).order_by('timestamp').all()[count-10:count]

    
 
    
 
    
