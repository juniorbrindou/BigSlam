from django.urls import path,include
from joueur import views




urlpatterns = [
    path('joueur', views.index, name='joueur'),
]