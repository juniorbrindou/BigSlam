from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
	data = {
	'rencontres':models.Game.objects.all(),
	}
	return render(request,'pages/programme.html',data)