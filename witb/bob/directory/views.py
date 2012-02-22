from django.template import Context, loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('layout.html')
    c = Context({
        'title': 'Directory of rooms and floors',
        'home' : False,
        'content' : 'listing.html'
    })
    return HttpResponse(t.render(c))
    