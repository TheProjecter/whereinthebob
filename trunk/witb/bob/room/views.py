from django.template import Context, loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('room.html')
    c = Context({
        'title': 'Room',
        'home' : False,
    })
    return HttpResponse(t.render(c))
    