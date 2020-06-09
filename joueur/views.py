from django.shortcuts import render, get_object_or_404
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
