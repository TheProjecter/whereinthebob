from bob.models import Room, Floor
from django.template import Context, loader, RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def index(request, id):
	room = get_object_or_404(Room, room_id=id)
	#comments = room.comments.model.objects.all()

	t = loader.get_template('room.html')
	c = RequestContext(request, {
		'title': 'Room',
		'home' : False,
		'room' : room,
		#'comments' : comments,
	})
	return HttpResponse(t.render(c))
    
