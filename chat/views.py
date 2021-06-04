from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

from chat.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def room(request, slug):
    print("2131")
    author = request.user.username
    print("author:L",type(author))
    roomName = slug
    print("slog:",slug)
    id =User.objects.get(username =roomName )
    room =Room.objects.get(nameRoom = id)
    messages = Message.last_10_messages(room)
    #admin hay not
    a = str(author)
    b=Room.objects.all()
     
    #---------------------
    context = {'room':room,'b':b,'a':a,'messages':messages,'room_name_json':mark_safe(json.dumps(slug)),'username':mark_safe(json.dumps(request.user.username))}
    if request.is_ajax():
        x=request.POST.get('x')
        s= request.user.username
        print("x:",x)
        # if s!="admin":
        #     print("huhuhuh")
        #     return render(request, 'chat/listAjax.html',context)
        # # # context = {'x',x:'room':room,'b':b,'a':a,'messages':messages,
        # # #             'room_name_json':mark_safe(json.dumps(slug)),
        # # #             'username':mark_safe(json.dumps(request.user.username))}
        # # print("mama")
        # else:
        #     print("i hate about")
        return render(request, 'chat/chatAjax.html',context)
    print("dmm")
    return render(request, 'chat/chat1.html',context)
 
def listAjax(request):
    b=Room.objects.all().order_by('-timestamp') 
    context={'b':b}
    print("ok")
    return render(request, 'chat/listAjax.html',context)