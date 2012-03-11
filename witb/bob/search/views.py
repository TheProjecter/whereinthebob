import re

from django.db.models import Q
from django.http import HttpResponse

from bob.models import Floor
from bob.models import Room
from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
	query_string = ''
	query_results = None

	if ('search_string' in request.GET) and request.GET['search_string'].strip():
		search_string = request.GET['search_string']
		query_string = get_query(search_string, ['type_id__type_name', 'description', 'room_id', 'room_name__name'])
		query_results = Room.objects.filter(query_string).order_by('rating')

	c = Context({
		'title': 'Search',
		'home' : False,
		'query_string': query_string, 
		'query_results': query_results
	})

	return render_to_response('search.html', c)

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
	query = None # Query to search for every search term        
	terms = normalize_query(query_string)
	for term in terms:
		or_query = None # Query to search for a given term in each field
		for field_name in search_fields:
			q = Q(**{"%s__icontains" % field_name: term})
			if or_query is None:
				or_query = q
			else:
				or_query = or_query | q
		if query is None:
			query = or_query
		else:
			query = query & or_query
	return query
