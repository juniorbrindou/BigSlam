from django.shortcuts import render
from . import models

# Create your views here.


def index(request):

	data = {
		'team' : models.Equipe.objects.all()
	}

	return render(request,'pages/big-slam.html', data)