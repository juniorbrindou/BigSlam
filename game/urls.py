from django.urls import path,include
from game import views




urlpatterns = [
    path('game', views.index, name='game'),
]