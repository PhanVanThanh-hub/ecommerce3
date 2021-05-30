from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from chat.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def room(request, slug):
    author = request.user.username
    print("author:L",type(author))
    roomName = slug
    id =User.objects.get(username =roomName )
    room =Room.objects.get(nameRoom = id)
    messages = Message.last_10_messages(room)
    for mesage in messages:
        print("s:",str(mesage))
        if str(mesage) == "admin":
            print("1:",mesage.author)
        else:
            print("ngu")
    #admin hay not
    a = str(author)
    #---------------------
    context = {'a':a,'messages':messages,'room_name_json':mark_safe(json.dumps(slug)),'username':mark_safe(json.dumps(request.user.username))}
    print("messgae:",messages)
    return render(request, 'chat/chat1.html',context)
 
