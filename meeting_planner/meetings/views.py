from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


def show_rooms(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": rooms})


def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room_details.html", {"room": room})
