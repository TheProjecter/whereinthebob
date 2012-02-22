from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    t = loader.get_template('layout.html')
    c = Context({
        'title': 'Home',
        'home' : True
    })
    return HttpResponse(t.render(c))
    
    #
    # This works for static pages (just get rid of
    # the template and the context and you're done):
    # 
    # return render_to_response('home.html')
    # 