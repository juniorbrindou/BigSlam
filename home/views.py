from django.shortcuts import render
from game.models import Game, Adversaire
from equipe.models import Equipe
# Create your views here.

def index(request):
	game = Game.objects.last()
	played = Game.objects.filter(has_played=True).order_by('id').reverse()
	big = Equipe.objects.first()
	adversaires = Adversaire.objects.all()
	lastAdversaire = Adversaire.objects.first()
	data = {
		'match':game,
		'adversaires':adversaires,
		'big':big,
		'played':played,
		'lastAdversaire':lastAdversaire,
	}
	return render(request,'pages/index.html',data)