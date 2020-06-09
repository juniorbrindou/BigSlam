from django.urls import path,include
from joueur import views

app_name = 'joueur'



urlpatterns = [
	# tous les joueurs player list
    path('', views.index, name='home'),

]