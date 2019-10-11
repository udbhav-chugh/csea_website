from django.shortcuts import render
from django.http import HttpResponse
from .models import Event_Model


def index(request):
	return render(request, 'home.html')

def events_view(request):
	qs = Event_Model.objects.all()
	context = {"object_list": qs}
	return 	render(request, "events2.html", context)

def events_search(request,name):
	qs = Event_Model.objects.filter(title__icontains=name)
	context = {"object_list": qs}
	return 	render(request, "events1.html", context)
