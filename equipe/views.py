from django.shortcuts import render
from . import models
from home import models

# Create your views here.


def index(request):

	data = {
		'team' : models.Equipe.objects.first(),

	}

	return render(request,'pages/big-slam.html', data)