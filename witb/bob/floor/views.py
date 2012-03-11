from bob.models import Floor
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def index(request, id):
        floor = get_object_or_404(Floor, floor_id=id)
        comments = floor.comments.model.objects.all()

        t = loader.get_template('room.html')
        c = Context({
                'title': 'Floor',
                'home' : False,
                'room' : floor,
                'comments' : comments,
                'id' : id       #kept only for the placeholder image;
        })
        return HttpResponse(t.render(c))

