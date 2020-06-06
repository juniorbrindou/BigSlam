from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'pages/player-list-gallery.html')

def single(request):
	return render(request,'pages/player-details.html')