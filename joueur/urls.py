from django.urls import path,include
from joueur import views




urlpatterns = [
    path('', views.index, name='home'),
]