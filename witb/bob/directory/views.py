from bob.models import Floor
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_list_or_404


def index(request):
    floors = get_list_or_404(Floor)
    t = loader.get_template('listing.html')
    c = Context({
        'title': 'Directory of rooms and floors',
        'home' : False,
        'floors' : floors
    })
    return HttpResponse(t.render(c))
    