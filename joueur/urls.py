from django.urls import path,include
from joueur import views




urlpatterns = [
	# tous les joueurs player list
    path('joueur', views.index, name='joueur'),

    # un joueur player details
    path('single', views.single, name ='single'),
]