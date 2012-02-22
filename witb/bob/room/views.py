from django.template import Context, loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('layout.html')
    c = Context({
        'title': 'Room',
        'home' : False,
        'content' : 'room.html'
    })
    return HttpResponse(t.render(c))
    