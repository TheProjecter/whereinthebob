# Create your views here.
from django.template import Context, loader
from bob.models import Comment
from django.http import HttpResponse


def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #t = loader.get_template('polls/index.html')
    #c = Context({
    #    'latest_poll_list': latest_poll_list,
    #})
    #return HttpResponse(t.render(c))
    
    return HttpResponse(Comment().getByGuid(333))