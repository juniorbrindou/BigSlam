from django.urls import path,include
from league import views



urlpatterns = [
	# tous les joueurs player list
    path('', views.index, name='league'),
]