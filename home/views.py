from django.shortcuts import render
from game import models
# Create your views here.

def index(request):
	game = models.Game.objects.last()
	data = {
		'match':game,
	}
	return render(request,'pages/index.html',data)