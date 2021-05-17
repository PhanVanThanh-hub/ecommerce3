import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.checks import messages
from .models import Message,Room
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
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
        roomName = data['roomName']
        message = data['message']
        print("33333333:")
        print("55555555:",roomName,':',author,':',message)
        await self.save(roomName,author,message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author':author
            }
        )
    @sync_to_async
    def save(self,roomName,author,message):
        roomName =User.objects.get(username =roomName )
        roomName= Room.objects.get(nameRoom =  roomName)
        author_user = User.objects.filter(username =author )[0]
        Message.objects.create(
            room = roomName,
            author = author_user,
            content = message
        )
    # Receive message from room group
    async def chat_message(self, event):
        print("22222")
        message = event['message']
        author = event['author']
        print("22222",message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'author':author
        }))
   
   