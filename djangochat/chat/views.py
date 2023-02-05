from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def room(request, room):
    # checkview HTML redirects to /room_name/?username=Tom
    # get variables from directed URL
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    
    return render(request, 'room.html', {
        'username':username, 
        'room':room, 
        'room_details': room_details
        }
    )

def checkview(request):
    # check if username exists in the database
    room = request.POST['room_name']
    username = request.POST['username']

    # if room exists in database
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else: # new room
        # create new room
        new_room = Room.objects.create(name=room)
        # add to database
        new_room.save()
        return redirect('/'+room+'/?username='+username)

# when a user clicks on submit message in a room
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(
        value=message,user = username, room = room_id
    )
    new_message.save()
    return HttpResponse('Message sent successfully!')

# updates the messages in the specified room
def getMessages(request,room):
    # gets messages for a specific room
    
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room= room_details.id)
    
    return JsonResponse({"messages":list(messages.values())})
