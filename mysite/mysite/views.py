from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime


def hello(request):
    return HttpResponse("Hello World")

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	html = "<html><body>It is now %s.</body></html>" % now
# 	return HttpResponse(html)

# def hours_ahead(request, offset):
# 	offset = int(offset)
# 	assert False
# 	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
# 	html = "<html><body>In %s hours, it will be %s.</body></html>" % (offset,dt)
# 	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

	context_dict = {}
	context_dict['hour_offset'] = offset
	context_dict['next_time'] = dt

	#return render(request, 'hours_ahead.html', {'hour_offset':offset}, {'next_time':dt})
	return render(request, 'hours_ahead.html', context_dict)

def display_books(request):
	html = "<html><body>Display Books.</body></html>" 
	return HttpResponse(html)


