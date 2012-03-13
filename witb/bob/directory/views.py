from bob.models import Floor, Room
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_list_or_404


def index(request):
    floors = get_list_or_404(Floor)
    rooms = get_list_or_404(Room)
    t = loader.get_template('listing.html')
    c = Context({
        'title': 'Directory of rooms and floors',
        'home' : False,
        'floors' : floors,
        'rooms' : rooms
    })
    return HttpResponse(t.render(c))
    