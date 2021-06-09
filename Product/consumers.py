import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.checks import messages
from ecom.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class CmtConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("opk")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
         
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data = json.loads(text_data)
        print("11111111:")
        author = data['form']
        user= data['us']
        roomName = data['roomName']
        rating = data['rating']
        message = data['message']
        print("33333333:")
        print("55555555:",roomName,':',author,':',message)
        await self.save(roomName,author,message,rating)
        print("lala:",author,':',data['pic'])
        pic = data['pic']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author':author,
                'user':user,
                'rating':rating,
                'pic':pic
           
            }
        )   
   
            
    @sync_to_async
    def save(self,roomName,author,message,rating):
        product = Product.objects.get(id = roomName)
        author = User.objects.filter(username =author )[0]
        author_user = Customer.objects.get(user = author)
        try:
            comment = Comment.objects.get(product = product,customer = author_user)
            comment.delete()
            
        except:
            print("oh mene")
        Comment.objects.create(
            product = product ,
            customer = author_user,
            comment  =message,
            rate = rating
        )
         
        comment = Comment.objects.all().filter( product = product)
        totalRate = 0.0
        for i in comment:
            totalRate = float(totalRate)+ float(i.rate)
        print("rate:",totalRate,':',comment.count())
        totalRate = totalRate/ comment.count()
        product.rate = totalRate
        product.save()
    # # Receive message from room group
    async def chat_message(self, event):
        print("22222")

        message = event['message']
        author = event['author']
        user = event['user']
        pic = event['pic']
        rating = event['rating']
        print("22222",message ,':',pic)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'author':author,
            'user':user,
            'rating':rating,
            'pic':pic
        }))
   
   