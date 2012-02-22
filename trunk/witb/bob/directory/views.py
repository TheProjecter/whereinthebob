from django.template import Context, loader
from django.http import HttpResponse


def index(request):
    t = loader.get_template('listing.html')
    c = Context({
        'title': 'Directory of rooms and floors',
        'home' : False
    })
    return HttpResponse(t.render(c))
    