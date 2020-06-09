from django.shortcuts import render
from . import models

# Create your views here.

def index(request):

	data = {

	'joueurs' : models.Joueur.objects.all(),
	'pivots' : models.Joueur.objects.filter(position=3),
	'arrieres' : models.Joueur.objects.filter(position=4),
	'ailiers' : models.Joueur.objects.filter(position=2),
	'meneurs' : models.Joueur.objects.filter(position=1),

	}
	return render(request,'pages/players.html',data)

def single(request):
	return render(request,'pages/player.html')