import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.checks import messages
from django.core.signals import request_finished
from .models import Message,Room
from django.contrib.auth import get_user_model
 
from ecom.models import *
User = get_user_model()
import datetime
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]
        status="onl"
        if str(self.user) !="admin":
            print("maybe")
            await self.getUser(status)
            message=status
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                }
            )
        await self.accept()
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
     

    async def disconnect(self, close_code):
        # Leave room group
        self.user = self.scope["user"]
        if str(self.user) !="admin":
            print("maybe")
            status ="off"
            message=status
            await self.getUser(status)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                }
            )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    @sync_to_async
    def getUser(self,status):
        roomName =User.objects.get(username =self.room_name )
        owns=Room.objects.get(nameRoom =  roomName)
        print("status:",status)
        if str(status)=="onl":
            owns.onl=True
            owns.save()
        else:
            owns.onl=False
            owns.save()
        

    async def receive(self, text_data):
        data = json.loads(text_data)
        author = data['form']
        roomName = data['roomName']
        message = data['message']    
        await self.save(roomName,author,message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author':author,
                'roomName':roomName
            }
        )
    
    @sync_to_async
    def save(self,roomName,author,message):
        roomName =User.objects.get(username =roomName )
        lastMess=Room.objects.get(nameRoom =  roomName)
        lastMess.content= message
        lastMess.timestamp=datetime.datetime.now()
        lastMess.save()
        roomName= Room.objects.get(nameRoom =  roomName)
        author_user = User.objects.filter(username =author )[0]
        Message.objects.create(
            room = roomName,
            author = author_user,
            content = message
        )
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        print("messgae:",message,'type:',type(message))
        if message=="onl" or message=="off":
            await self.send(text_data=json.dumps({
            'message': message,
            
        }))
        else:
            author = event['author']
            roomName = event['roomName']
            nameRoom=""
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'author':author,
                'roomName':roomName
            }))
   
   