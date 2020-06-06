from django.urls import path,include
from joueur import views

# app_name = 'joueur'



urlpatterns = [
	# tous les joueurs player list
    path('', views.index, name='joueur'),

    # un joueur player details
    path('single', views.single, name ='single'),
]