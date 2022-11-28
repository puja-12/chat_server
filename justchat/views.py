from django.shortcuts import render

from justchat.models import Chat


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    # if not request.user.is_authenticated:
    #     return redirect('/chat/')

    room = Chat.objects.filter(room_name=room_name).first()
    chats=[]
    if room:
        chats=Chat.objects.filter(room_name=room)
    else:
        message = Chat(room_name=room_name)
        message.save()
    return render(request, 'chat/room.html', context={
        'room_name': room_name,'chats':chats
    })



